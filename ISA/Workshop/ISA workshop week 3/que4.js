const prompt = require('prompt-sync')();
function give_me_something(a){
    console.log("Something"+" "+ a +".");
}
let abc = parseInt(prompt("enter the sentence u want to add 'something' as prefixx:"));
give_me_something(abc);