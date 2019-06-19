// quarter: 25 cents / $0.25
// dime: 10 cents / $0.10
// nickel: 5 cents / $0.05
// penny: 1 cent / $0.01



function changeEnough(values, total_sum){
    let money_values = [0.25, 0.1, 0.05, 0.01];

    let total_value = 0;
    for(let i = 0; i < values.length; i++){
        total_value += values[i] * money_values[i]; 
    }
    
    return (total_value >= total_sum ? true : false)

}

console.log(changeEnough([2, 100, 0, 0], 14.11));

console.log(changeEnough([0, 0, 20, 5], 0.75));

console.log(changeEnough([30, 40, 20, 5], 12.55));

console.log(changeEnough([10, 0, 0, 50], 3.85));

console.log(changeEnough([1, 0, 5, 219], 19.99));
