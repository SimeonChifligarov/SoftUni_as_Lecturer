// function traveling(input) {  // "text" 'text1'
//     let i = 0; 
//     let destination = input[i];
//     i++;
//     let moneyNeeded = Number(input[i]);
//     i++;
//     let currentSum = 0;
//     while (true) {
//         if (destination == "End") {
//             break;
//         }

//         currentSum += Number(input[i]);
//         if (currentSum >= moneyNeeded) {
//             console.log(`Going to ${destination}!`);
//             i++;
//             if (input[i] == "End") {
//                 break;
//             }
//             destination = input[i];
//             i++;
//             moneyNeeded = input[i];
//             currentSum = 0;
//         }
//         i++;
//     }
// }

// traveling(['End']);

function solve(input) {
    let currentCase = input[0]

    if (currentCase == '22') {
        console.log(`neshto si koeto trqbwa da e rezultat ot logikata`);
    } else if (currentCase == '33') {
        console.log(`neshto si suvsem drugo`);
    }

}


solve(['22']);
solve(['33'])