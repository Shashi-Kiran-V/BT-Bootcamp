const readline = require('readline-sync');

let cart = [];
let addMore = true;

// LAB 1: Add Items
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

// Calculate grand total
let grandTotal = cart.reduce((sum, item) => sum + item.totalPrice, 0);

// Display cart as table
console.log("\n=== Cart Details ===");
console.log(
  `${"S.No".padEnd(6)} | ${"Code".padEnd(10)} | ${"Description".padEnd(20)} | ${"Qty".padEnd(5)} | ${"Price/unit".padEnd(12)} | ${"Total".padEnd(10)}`
);
console.log("-".repeat(75));
cart.forEach((item, index) => {
  console.log(
    `${(index + 1).toString().padEnd(6)} | ${item.itemCode.padEnd(10)} | ${item.description.padEnd(20)} | ${item.quantity.toString().padEnd(5)} | ${item.pricePerUnit.toFixed(2).padEnd(12)} | ${item.totalPrice.toFixed(2).padEnd(10)}`
  );
});
console.log("-".repeat(75));
console.log("Grand Total:".padEnd(59) + grandTotal.toFixed(2));

// LAB 2: Apply Membership Discount
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

let discountAmount = grandTotal * discountRate;
let discountedTotal = grandTotal - discountAmount;

console.log("\n=== Discount Details ===");
console.log(`Membership Type: ${membershipType.charAt(0).toUpperCase() + membershipType.slice(1)}`);
console.log(`Discount Rate: ${(discountRate * 100).toFixed(0)}%`);
console.log(`Discount Amount: ${discountAmount.toFixed(2)}`);
console.log(`Total after Discount: ${discountedTotal.toFixed(2)}`);

// LAB 3: Apply GST and Platform Fee
const gstRate = 0.18;          // 18% GST
const platformFeeRate = 0.002; // 0.2% platform fee

let gstAmount = discountedTotal * gstRate;
let platformFee = discountedTotal * platformFeeRate;
let totalWithTax = discountedTotal + gstAmount + platformFee;

console.log("\n=== Tax and Platform Fee Details ===");
console.log(`GST (18%):`.padEnd(30) + gstAmount.toFixed(2));
console.log(`Platform Fee (0.2%):`.padEnd(30) + platformFee.toFixed(2));
console.log("-".repeat(40));
console.log(`Total Amount Payable:`.padEnd(30) + totalWithTax.toFixed(2));
