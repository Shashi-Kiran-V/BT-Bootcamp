const readline = require('readline-sync');

let cart = [];
let addMore = true;

while (addMore) {
  let itemCode = readline.question("Enter item code: ");
  let description = readline.question("Enter item description: ");
  let quantity = parseFloat(readline.question("Enter quantity: "));
  let pricePerUnit = parseFloat(readline.question("Enter price per unit: "));

  let totalPrice = quantity * pricePerUnit;

  cart.push({
    itemCode,
    description,
    quantity,
    pricePerUnit,
    totalPrice
  });

  let more = readline.question("Do you want to add another item? (yes/no): ").toLowerCase();
  addMore = more === "yes";
}

// Calculate grand total
let grandTotal = cart.reduce((sum, item) => sum + item.totalPrice, 0);

// Display cart as table
console.log("\n=== Cart Details ===");

// Table header
console.log(
  `${"S.No".padEnd(6)} | ${"Code".padEnd(10)} | ${"Description".padEnd(20)} | ${"Qty".padEnd(5)} | ${"Price/unit".padEnd(12)} | ${"Total".padEnd(10)}`
);
console.log("-".repeat(75));

// Table rows
cart.forEach((item, index) => {
  console.log(
    `${(index + 1).toString().padEnd(6)} | ${item.itemCode.padEnd(10)} | ${item.description.padEnd(20)} | ${item.quantity.toString().padEnd(5)} | ${item.pricePerUnit.toFixed(2).padEnd(12)} | ${item.totalPrice.toFixed(2).padEnd(10)}`
  );
});

console.log("-".repeat(75));
console.log("Grand Total:".padEnd(59) + grandTotal.toFixed(2));
