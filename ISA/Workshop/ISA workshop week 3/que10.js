const prompt = require("prompt-sync")();
function weeklySalary(weekArray){
    let total = 0;
    for (let i=0;i<7;i++){
        if (i<=4){
            if (weekArray[i]<=8){
                total += 10*weekArray[i];
            } else {
                total += 80 + 15*(weekArray[i]-8);
            }
        } else {
            if (weekArray[i]<=8){
                total += 2*(10*weekArray[i]);
            } else {
                total += 2*(80 + 15*(weekArray[i]-8));
            }
        }
    }
    return ("$"+total);
}
let hours = [];
console.log("Enter the wroking hours for each day of the week:\n");
for (let i=1;i<=7;i++){
    let Time = parseInt(prompt(`Day ${i}:`));
    hours.push(Time);
} 
console.log("Total weekly salary =",weeklySalary(hours));