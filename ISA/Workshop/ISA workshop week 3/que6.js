const prompt = require('prompt-sync')();
let num = parseInt(prompt("enter the number to check:"));
if (num>0){
    console.log(num + " is a positive number.");
} else if (num<0) {
    console.log(num + " is a negative number.");
} else {
    console.log(num + " is zero.");
}