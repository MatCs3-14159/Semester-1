const prompt = require('prompt-sync')();
function print_array(x){
    var new_array = [];
    for (let i=1;i<=x;i++){
        new_array.push(i);
    }
    return new_array;
}
let num = parseInt (prompt ("Enter the number:"))
console.log(print_array(num));