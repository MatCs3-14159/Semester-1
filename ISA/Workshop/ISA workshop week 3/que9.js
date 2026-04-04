const prompt = require("prompt-sync")();
function getTotalPrice(groceries){
    let total = 0;
    for (let i=0;i<groceries.length;i++){
        total += groceries[i].quantity * groceries[i].price ;
    }
    return parseFloat(total.toFixed(2));
}
let n = parseInt(prompt("How many groceries do u want to buy? : "));
let groceries = [];
for (let i=0;i<n;i++){
    console.log(`\nEnter the details of product ${i}:`);
    let product = prompt("Product name:");
    let quantity = parseInt(prompt("Product quantity:"));
    let price = parseFloat(prompt("Product price:"));
    groceries.push({ 
        product: product,
        quantity: quantity,
        price: price 
    });
}
console.log("\nTotal amount : Rs." + getTotalPrice(groceries));