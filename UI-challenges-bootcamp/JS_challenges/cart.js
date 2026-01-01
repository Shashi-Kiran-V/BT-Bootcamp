const readline = require('readline-sync');
const fs = require('fs');

class ValidationError extends Error {
  constructor(message) {
    super(message);
    this.name = "ValidationError";
  }
}

let cart = [];
let addMore = true;

try {
  // ===== LAB 1: Add Items to Cart with Validation =====
  while (addMore) {
    let itemCode = readline.question("Enter item code: ");
    let description = readline.question("Enter item description: ");
    
    let quantity = parseFloat(readline.question("Enter quantity: "));
    if (isNaN(quantity) || quantity <= 0) throw new ValidationError("Quantity must be a number greater than 0.");
    
    let pricePerUnit = parseFloat(readline.question("Enter price per unit: "));
    if (isNaN(pricePerUnit) || pricePerUnit <= 0) throw new ValidationError("Price must be a number greater than 0.");

    let totalPrice = quantity * pricePerUnit;
    cart.push({ itemCode, description, quantity, pricePerUnit, totalPrice });

    addMore = readline.question("Do you want to add another item? (yes/no): ").toLowerCase() === "yes";
  }

  if (cart.length === 0) throw new ValidationError("Cart cannot be empty.");

  // ===== LAB 2: Membership Discount =====
  let membershipType = "None";
  let discountRate = 0;
  let isMember = readline.question("Are you a member? (yes/no): ").toLowerCase();
  if (isMember === "yes") {
    membershipType = readline.question("Enter membership type (Silver/Gold/Platinum): ").toLowerCase();
    if (membershipType === "silver") discountRate = 0.05;
    else if (membershipType === "gold") discountRate = 0.10;
    else if (membershipType === "platinum") discountRate = 0.15;
    else {
      console.log("Invalid membership type. No discount applied.");
      discountRate = 0;
      membershipType = "None";
    }
  }

  // ===== LAB 3: GST & Platform Fee =====
  const gstRate = 0.18;
  const platformFeeRate = 0.002;

  // ===== LAB 4: Payment Mode Charges =====
  let paymentMode = readline.question("Enter payment mode (Card/UPI/Cash/Other): ").toLowerCase();
  if (!paymentMode) throw new ValidationError("Payment mode cannot be empty.");

  let surcharge = 0;
  let convenienceFee = 0;

  // ===== CALCULATIONS =====
  let grandTotal = cart.reduce((sum, item) => sum + item.totalPrice, 0);
  let discountAmount = grandTotal * discountRate;
  let discountedTotal = grandTotal - discountAmount;

  let gstAmount = discountedTotal * gstRate;
  let platformFee = discountedTotal * platformFeeRate;
  let totalWithTax = discountedTotal + gstAmount + platformFee;

  if (paymentMode === "card" && totalWithTax < 1000) {
    surcharge = totalWithTax * 0.025;
  } else if (paymentMode !== "card") {
    convenienceFee = totalWithTax * 0.01;
  }

  let finalAmount = totalWithTax + surcharge + convenienceFee;

  // ===== LAB 5 & 8: Invoice & Email Validation =====
  let invoiceNumber = "INV-" + Math.floor(Math.random() * 1000000);
  let invoiceDate = new Date();

  let emailPattern = /^[a-zA-Z0-9._%+-]+@karunya\.edu$/;
  let email = readline.question("Enter your email (@karunya.edu): ");
  while (!emailPattern.test(email)) {
    console.log("Invalid email format. Please enter a valid @karunya.edu email.");
    email = readline.question("Enter your email (@karunya.edu): ");
  }

  console.log(`Thank you! A confirmation has been sent to ${email}.`);

  let invoiceData = {
    invoiceNumber,
    invoiceDate: invoiceDate.toISOString(),
    cartItems: cart,
    subtotal: grandTotal,
    discountRate,
    discountAmount,
    discountedTotal,
    gstRate,
    gstAmount,
    platformFeeRate,
    platformFee,
    totalWithTax,
    paymentMode,
    surcharge,
    convenienceFee,
    finalAmount
  };

  // ===== LAB 6: Optional save =====
  let saveOption = readline.question("Do you want to save the invoice locally as JSON? (yes/no): ").toLowerCase();
  if (saveOption === "yes") {
    let fileName = `${invoiceNumber}.json`;
    fs.writeFileSync(fileName, JSON.stringify(invoiceData, null, 2));
    console.log(`Invoice saved locally as ${fileName}`);
  }

  // ===== Display Invoice =====
  console.log("\n==========================================");
  console.log(`Invoice No: ${invoiceNumber}`);
  console.log(`Date: ${invoiceDate.toLocaleString()}`);
  console.log(`Email: ${email}`);
  console.log("------------------------------------------");
  console.log(`${"S.No".padEnd(6)} | ${"Code".padEnd(10)} | ${"Description".padEnd(20)} | ${"Qty".padEnd(5)} | ${"Price/unit".padEnd(12)} | ${"Total".padEnd(10)}`);
  console.log("-".repeat(75));
  cart.forEach((item, index) => {
    console.log(
      `${(index+1).toString().padEnd(6)} | ${item.itemCode.padEnd(10)} | ${item.description.padEnd(20)} | ${item.quantity.toString().padEnd(5)} | ${item.pricePerUnit.toFixed(2).padEnd(12)} | ${item.totalPrice.toFixed(2).padEnd(10)}`
    );
  });
  console.log("-".repeat(75));
  console.log(`Subtotal:`.padEnd(59) + `₹${grandTotal.toFixed(2)}`);
  console.log(`Discount (${(discountRate*100).toFixed(0)}%):`.padEnd(59) + `₹${discountAmount.toFixed(2)}`);
  console.log(`Total after Discount:`.padEnd(59) + `₹${discountedTotal.toFixed(2)}`);
  console.log(`GST (18%):`.padEnd(59) + `₹${gstAmount.toFixed(2)}`);
  console.log(`Platform Fee (0.2%):`.padEnd(59) + `₹${platformFee.toFixed(2)}`);
  console.log(`Total with Tax & Fee:`.padEnd(59) + `₹${totalWithTax.toFixed(2)}`);
  console.log(`Payment Mode:`.padEnd(59) + `${paymentMode.charAt(0).toUpperCase() + paymentMode.slice(1)}`);
  console.log(`Surcharge:`.padEnd(59) + `₹${surcharge.toFixed(2)}`);
  console.log(`Convenience Fee:`.padEnd(59) + `₹${convenienceFee.toFixed(2)}`);
  console.log("-".repeat(75));
  console.log(`FINAL AMOUNT PAYABLE:`.padEnd(59) + `₹${finalAmount.toFixed(2)}`);
  console.log("==========================================");
  console.log("          PAYMENT SUCCESSFUL!             ");
  console.log("           INVOICE GENERATED              ");
  console.log("==========================================\n");

} catch (err) {
  if (err instanceof ValidationError) {
    console.log(`Validation Error: ${err.message}`);
  } else {
    console.log(`Unexpected Error: ${err.message}`);
  }
} finally {
  console.log("Checkout process completed. Thank you for shopping at Karazon.com!");
}
