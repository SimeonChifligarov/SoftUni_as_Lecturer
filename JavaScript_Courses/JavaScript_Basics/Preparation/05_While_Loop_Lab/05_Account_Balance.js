function accountBalance(input) {
    let balance = 0;

    i = 0;
    while (true) {
        let currentCommand = input[i];
        i++;

        if (currentCommand == "NoMoreMoney") {
            break;
        }

        currentAmount = Number(currentCommand);
        if (currentAmount < 0) {
            console.log('Invalid operation!');
            break;
        }

        balance += currentAmount;
        console.log(`Increase: ${currentAmount.toFixed(2)}`);
    }

    console.log(`Total: ${balance.toFixed(2)}`);
}


// accountBalance(["5.51",
//     "69.42",
//     "100",
//     "NoMoreMoney"]);
