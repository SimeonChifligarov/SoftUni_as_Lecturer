function vacation(input) {
    let moneyNeeded = Number(input[0]);
    let moneyReal = Number(input[1]);

    let i = 2;

    let consecutiveSpendingDays = 0;
    let totalDays = 0;

    while (true) {
        let currentAction = input[i];
        let currentAmount = Number(input[i + 1]);

        totalDays++;

        if (currentAction == "spend") {
            consecutiveSpendingDays++;
            moneyReal -= currentAmount;
            if (moneyReal < 0) {
                moneyReal = 0;
            }
        } else if (currentAction == "save") {
            moneyReal += currentAmount;
            consecutiveSpendingDays = 0;
        }

        if (consecutiveSpendingDays == 5) {
            console.log("You can't save the money.");
            console.log(totalDays);
            break;
        }

        if (moneyReal >= moneyNeeded) {
            console.log(`You saved the money for ${totalDays} days.`);
            break;
        }

        i += 2;
    }
}


// vacation([
//     "2000",
//     "1000",
//     "spend",
//     "1200",
//     "save",
//     "2000"
// ]);
