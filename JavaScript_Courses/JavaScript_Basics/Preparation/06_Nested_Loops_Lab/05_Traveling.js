function traveling(input) {
    let i = 0;

    while (true) {
        let currentCommand = input[i];

        if (currentCommand == "End") {
            break;
        }

        i++;
        let currentBudget = Number(input[i]);

        while (true) {
            i++;
            let currentSum = Number(input[i]);
            currentBudget -= currentSum;
            if (currentBudget <= 0) {
                console.log(`Going to ${currentCommand}!`);
                i++;
                break;
            } 
        }
    }
}


// function traveling(input) {
//     for (let i = 0; i < input.length; i++) {
//         let currentCommand = input[i];
//         if (isNaN(currentCommand) && (currentCommand != "End")) {
//             console.log(`Going to ${currentCommand}!`);
//         }
//     }
// }


// traveling([
//     "Greece",
//     "1000",
//     "200",
//     "200",
//     "300",
//     "100",
//     "150",
//     "240",
//     "Spain",
//     "1200",
//     "300",
//     "500",
//     "193",
//     "423",
//     "End",
// ]);
