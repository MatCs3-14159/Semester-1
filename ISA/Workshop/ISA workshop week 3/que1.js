const prompt = require('prompt-sync')();
function check_even_positive(x) {
     if (x>0 && x % 2 == 0) {
        console.log (x + " is both even and positive.");
    }
    else {
        console.log (x + " is either odd or negative.");
    }
}
let num = parseInt (prompt ("Enter the number:"))
check_even_positive(num);