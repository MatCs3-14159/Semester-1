function count_true(x){
    let count = 0 ;
    for (let i=0;i<x.length;i++){
        if (x[i] === true){
            count++;
        }
        else{
            continue;
        }
    }
    return count;
}
let array = [1,2,3,4,5,6,7,true,18920,true,false];
console.log(count_true(array));
