const prompt = require('prompt-sync')();
function div46_check(x){
    if (x%4 == 0 && x%6 == 0 && x%8 != 0)
    {
        console.log(x + " is divisible by 4 and 6 but not by 8.");
    } else {
        console.log("try another.");
    }
}
let num = parseInt(prompt("enter the number to check:"));
div46_check(num);