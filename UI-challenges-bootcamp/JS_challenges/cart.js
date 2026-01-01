const readline = require('readline-sync');
const fs = require('fs');

// ===== LAB 1: Add Items to Cart =====
let cart = [];
let addMore = true;

while (addMore) {
  let itemCode = readline.question("Enter item code: ");
  let description = readline.question("Enter item description: ");
  let quantity = parseFloat(readline.question("Enter quantity: "));
  let pricePerUnit = parseFloat(readline.question("Enter price per unit: "));

  let totalPrice = quantity * pricePerUnit;

  cart.push({ itemCode, description, quantity, pricePerUnit, totalPrice });

  let more = readline.question("Do you want to add another item? (yes/no): ").toLowerCase();
  addMore = more === "yes";
}

// ===== LAB 2: Apply Membership Discount =====
let membershipType = "None";
let discountRate = 0;

let isMember = readline.question("\nAre you a member? (yes/no): ").toLowerCase();
if (isMember === "yes") {
  membershipType = readline.question("Enter membership type (Silver/Gold/Platinum): ").toLowerCase();
  if (membershipType === "silver") discountRate = 0.05;
  else if (membershipType === "gold") discountRate = 0.10;
  else if (membershipType === "platinum") discountRate = 0.15;
  else {
    console.log("Invalid membership type. No discount applied.");
    discountRate = 0;
  }
}

// ===== LAB 3: GST and Platform Fee =====
const gstRate = 0.18;          // 18% GST
const platformFeeRate = 0.002; // 0.2% platform fee

// ===== LAB 4: Payment Mode Charges =====
let paymentMode = readline.question("\nEnter payment mode (Card/UPI/Cash/Other): ").toLowerCase();

// ===== CALCULATIONS =====
let grandTotal = cart.reduce((sum, item) => sum + item.totalPrice, 0);
let discountAmount = grandTotal * discountRate;
let discountedTotal = grandTotal - discountAmount;

let gstAmount = discountedTotal * gstRate;
let platformFee = discountedTotal * platformFeeRate;
let totalWithTax = discountedTotal + gstAmount + platformFee;

let surcharge = 0;
let convenienceFee = 0;

if (paymentMode === "card" && totalWithTax < 1000) {
  surcharge = totalWithTax * 0.025; // 2.5% card surcharge
} else if (paymentMode !== "card") {
  convenienceFee = totalWithTax * 0.01; // 1% convenience fee
}

let finalAmount = totalWithTax + surcharge + convenienceFee;

// ===== LAB 5: Generate Invoice =====
let invoiceDate = new Date();
let invoiceNumber = "INV-" + Math.floor(Math.random() * 1000000);

// ===== PRINT INVOICE =====
console.log("\n\n==========================================");
console.log("          KARAZON.COM INVOICE             ");
console.log("==========================================");
console.log(`Invoice No: ${invoiceNumber}`);
console.log(`Date: ${invoiceDate.toLocaleString()}`);
console.log("------------------------------------------");

// Table Header
console.log(`${"S.No".padEnd(6)} | ${"Code".padEnd(10)} | ${"Description".padEnd(20)} | ${"Qty".padEnd(5)} | ${"Price/unit".padEnd(12)} | ${"Total".padEnd(10)}`);
console.log("-".repeat(75));

// Table Rows
cart.forEach((item, index) => {
  console.log(
    `${(index + 1).toString().padEnd(6)} | ${item.itemCode.padEnd(10)} | ${item.description.padEnd(20)} | ${item.quantity.toString().padEnd(5)} | ${item.pricePerUnit.toFixed(2).padEnd(12)} | ${item.totalPrice.toFixed(2).padEnd(10)}`
  );
});
console.log("-".repeat(75));

// Totals & Fees
console.log(`Subtotal:`.padEnd(59) + grandTotal.toFixed(2));
console.log(`Discount (${(discountRate*100).toFixed(0)}%):`.padEnd(59) + discountAmount.toFixed(2));
console.log(`Total after Discount:`.padEnd(59) + discountedTotal.toFixed(2));
console.log(`GST (18%):`.padEnd(59) + gstAmount.toFixed(2));
console.log(`Platform Fee (0.2%):`.padEnd(59) + platformFee.toFixed(2));
console.log(`Total with Tax & Fee:`.padEnd(59) + totalWithTax.toFixed(2));
console.log(`Payment Mode: ${paymentMode.charAt(0).toUpperCase() + paymentMode.slice(1)}`);
console.log(`Surcharge:`.padEnd(59) + surcharge.toFixed(2));
console.log(`Convenience Fee:`.padEnd(59) + convenienceFee.toFixed(2));
console.log("-".repeat(75));
console.log(`FINAL AMOUNT PAYABLE:`.padEnd(59) + finalAmount.toFixed(2));
console.log("==========================================");
console.log("          PAYMENT SUCCESSFUL!             ");
console.log("           INVOICE GENERATED              ");
console.log("==========================================\n\n");

// ===== LAB 6: Email Simulation & Local Save =====
let emailAddress = readline.question("\nEnter your email (must be @karunya.edu): ");

while (!emailAddress.endsWith("@karunya.edu")) {
  console.log("Invalid email. Must be a valid @karunya.edu address.");
  emailAddress = readline.question("Enter your email: ");
}

// Prepare invoice data in JSON
let invoiceData = {
  invoiceNumber: invoiceNumber,
  invoiceDate: invoiceDate.toISOString(),
  items: cart,
  subtotal: grandTotal,
  discountRate: discountRate,
  discountAmount: discountAmount,
  discountedTotal: discountedTotal,
  gstRate: gstRate,
  gstAmount: gstAmount,
  platformFeeRate: platformFeeRate,
  platformFee: platformFee,
  totalWithTax: totalWithTax,
  paymentMode: paymentMode,
  surcharge: surcharge,
  convenienceFee: convenienceFee,
  finalAmount: finalAmount
};

// Simulate sending email
console.log(`\nInvoice sent to ${emailAddress} successfully!`);

// Optional: save invoice locally as JSON
let saveOption = readline.question("Do you want to save the invoice locally as JSON? (yes/no): ").toLowerCase();
if (saveOption === "yes") {
  let fileName = `${invoiceNumber}.json`;
  fs.writeFileSync(fileName, JSON.stringify(invoiceData, null, 2));
  console.log(`Invoice saved locally as ${fileName}`);
}

// Display invoice JSON on console
console.log("\n=== Invoice JSON Preview ===");
console.log(JSON.stringify(invoiceData, null, 2));

console.log("\nThank you for shopping at Karazon.com!");
console.log("Payment Successful! Invoice Generated.");