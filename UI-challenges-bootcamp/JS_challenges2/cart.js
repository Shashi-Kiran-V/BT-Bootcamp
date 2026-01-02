/* ================= LAB 9: Custom Validation Error ================= */
class ValidationError extends Error {
  constructor(message) {
    super(message);
    this.name = "ValidationError";
  }
}

/* ================= LAB 10: Closure-based Discount ================= */
function getDiscountFunction(type) {
  const rates = {
    silver: 0.05,
    gold: 0.10,
    platinum: 0.15,
    none: 0
  };
  return function(baseAmount) {
    const rate = rates[type.toLowerCase()] ?? 0;
    return {
      discountRate: rate,
      discountAmount: baseAmount * rate,
      discountedTotal: baseAmount - baseAmount * rate
    };
  };
}

/* ================= LAB 12: Inventory Check (Skip if stock insufficient) ================= */
async function validateAndAddItem(item) {
  return new Promise((resolve) => {
    const inventory = {
      "ITEM1": 10,
      "ITEM2": 5,
      "ITEM3": 20
    };
    let stock = inventory[item.itemCode.toUpperCase()] ?? 0;
    if (item.quantity <= stock) {
      resolve(true); // Item OK, add to cart
    } else {
      alert(`Insufficient stock for ${item.itemCode}. Skipping this item.`);
      resolve(false); // Skip item
    }
  });
}

/* ================= LAB 11: Async Payment ================= */
async function processPayment(finalAmount, paymentMode) {
  console.log(`Processing ${paymentMode} payment for ₹${finalAmount.toFixed(2)}...`);
  return new Promise((resolve) => {
    setTimeout(() => {
      console.log("Payment confirmed ✅");
      resolve({ status: "success", mode: paymentMode, amount: finalAmount });
    }, 2000);
  });
}

/* ================= LAB 13: Callback for Billing Completion ================= */
function completeBilling(callback, invoiceData) {
  callback(invoiceData);
}

/* ================= MAIN FLOW ================= */
(async function main() {
  try {
    /* ===== LAB 7: Persistent Cart ===== */
    let previousInvoice = localStorage.getItem("karazon_invoice");
    let cart = [];
    let subtotal = 0;

    if (previousInvoice) {
      let resume = confirm("Previous cart found. Resume previous cart?");
      if (resume) {
        previousInvoice = JSON.parse(previousInvoice);
        cart = previousInvoice.cart;
        subtotal = previousInvoice.subtotal;
        console.log("Previous cart loaded:", cart);
      }
    }

    /* ===== LAB 1: Add Items ===== */
    let addMore = true;
    while (addMore) {
      let itemCode = prompt("Enter item code (e.g., ITEM1):");
      let description = prompt("Enter item description:");
      let quantity = Number(prompt("Enter quantity:"));
      if (isNaN(quantity) || quantity <= 0)
        throw new ValidationError("Quantity must be greater than 0");

      let price = Number(prompt("Enter price per unit:"));
      if (isNaN(price) || price <= 0)
        throw new ValidationError("Price must be greater than 0");

      let item = { itemCode, description, quantity, price, total: quantity * price };

      /* ===== LAB 12: Inventory Lookup ===== */
      const valid = await validateAndAddItem(item);
      if (valid) {
        cart.push(item);
        subtotal = cart.reduce((s, i) => s + i.total, 0);
      }

      addMore = prompt("Add another item? (yes/no)").toLowerCase() === "yes";
    }

    if (cart.length === 0)
      throw new ValidationError("Cart cannot be empty");

    /* ===== LAB 10: Membership Discount ===== */
    let membershipType = "none";
    if (prompt("Are you a member? (yes/no)").toLowerCase() === "yes") {
      membershipType = prompt("Membership type (Silver/Gold/Platinum):");
    }

    const discountFn = getDiscountFunction(membershipType);
    const discountInfo = discountFn(subtotal);

    /* ===== LAB 3: GST & Platform Fee ===== */
    const gst = discountInfo.discountedTotal * 0.18;
    const platformFee = discountInfo.discountedTotal * 0.002;
    let totalWithTax = discountInfo.discountedTotal + gst + platformFee;

    /* ===== LAB 4: Payment Mode ===== */
    let paymentMode = prompt("Payment mode (Card/UPI/Cash):").toLowerCase();
    if (!paymentMode)
      throw new ValidationError("Payment mode cannot be empty");

    let surcharge = 0;
    let convenienceFee = 0;

    if (paymentMode === "card" && totalWithTax < 1000)
      surcharge = totalWithTax * 0.025;
    else if (paymentMode !== "card")
      convenienceFee = totalWithTax * 0.01;

    let finalAmount = totalWithTax + surcharge + convenienceFee;

    /* ===== LAB 11: Async Payment Confirmation ===== */
    const paymentResult = await processPayment(finalAmount, paymentMode);

    /* ===== LAB 8: Email Validation & Notification ===== */
    const emailRegex = /^[a-zA-Z0-9._%+-]+@karunya\.edu$/;
    let email = prompt("Enter email (@karunya.edu):");
    while (!emailRegex.test(email)) {
      alert("Invalid email format");
      email = prompt("Enter valid email (@karunya.edu):");
    }
    console.log(`Invoice confirmation sent to ${email}`);

    /* ===== LAB 5 & 6: Invoice Generation & Local Save ===== */
    let invoice = {
      invoiceNo: "INV-" + Math.floor(Math.random() * 100000),
      date: new Date().toLocaleString(),
      email,
      cart,
      subtotal,
      discount: discountInfo.discountAmount,
      gst,
      platformFee,
      surcharge,
      convenienceFee,
      finalAmount,
      paymentStatus: paymentResult.status
    };

    if (confirm("Save invoice locally?")) {
      localStorage.setItem("karazon_invoice", JSON.stringify(invoice));
      console.log("Invoice saved in localStorage ✅");
    }

    /* ===== LAB 13: Callback to Display Invoice ===== */
    completeBilling((inv) => {
      console.clear();
      console.log("========== KARAZON INVOICE ==========");
      console.table(inv.cart);
      console.log("Subtotal:", inv.subtotal);
      console.log("Discount:", inv.discount);
      console.log("GST:", inv.gst);
      console.log("Platform Fee:", inv.platformFee);
      console.log("Surcharge:", inv.surcharge);
      console.log("Convenience Fee:", inv.convenienceFee);
      console.log("FINAL AMOUNT PAYABLE:", inv.finalAmount);
      console.log("Payment Status:", inv.paymentStatus);
      console.log("====================================");
      console.log("PAYMENT SUCCESSFUL ✅");
      console.log("INVOICE GENERATED");
    }, invoice);

  } catch (err) {
    if (err instanceof ValidationError) alert("Validation Error: " + err.message);
    else alert("Unexpected Error: " + err.message);
  } finally {
    console.log("Thank you for shopping at Karazon.com 🎉");
  }
})();
