//Leetcode 1502


const numbersArray = [1,9,7,5,3]; 

const progression = function (arr) {
    arr = arr.sort((a,b) => {
        return a-b;
    })
    console.log(arr);
    let difference = arr[1] - arr[0];
    console.log(`difference is: ${difference}`);

    for(let i = 0; i < arr.length; i++) {
        if(arr[i+1] != undefined) {
            if(arr[i+1] - arr[i] != difference) {
                console.log(`Subtracting ${arr[i]} and ${arr[i+1]}`)
                return false
            }
            console.log(`array index is ${i}`)
            console.log(`Subtracting ${arr[i]} and ${arr[i+1]}`)
            
        }
        }
    return true

    // iterate over two elements in array. subtract them, determine if answer is equal to difference. 
}

console.log(progression(numbersArray));