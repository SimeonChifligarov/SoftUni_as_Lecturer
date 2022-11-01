function vacation(input) {  // (["2000","1000","spend","1200","save","2000"]);
    let moneyNeeded = Number(input[0]);
    let moneyReal = Number(input[1]);

    
    let consecutiveSpendingDays = 0;
    let totalDays = 0;
    
    let i = 2;
    while (true) {
        let currentAction = input[i];
        i++;
        let currentAmount = Number(input[i]);
        i++;

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

    }
}


vacation([
    "2000",
    "1000",
    "spend",
    "1200",
    "save",
    "2000"
]);