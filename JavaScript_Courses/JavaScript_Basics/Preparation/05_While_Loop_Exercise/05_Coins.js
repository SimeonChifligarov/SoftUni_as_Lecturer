function coins(input) {
    let moneyAmount = Number(input[0]);
    let coinsCount = 0;

    let currentAmountInCents = Math.round(moneyAmount * 100);
    // let currentAmountInCents = moneyAmount * 100;
    // console.log(currentAmountInCents);

    while (currentAmountInCents > 0) {
        if (currentAmountInCents >= 200) {
            currentAmountInCents -= 200;
        } else if (currentAmountInCents >= 100) {
            currentAmountInCents -= 100;
        } else if (currentAmountInCents >= 50) {
            currentAmountInCents -= 50;
        } else if (currentAmountInCents >= 20) {
            currentAmountInCents -= 20;
        } else if (currentAmountInCents >= 10) {
            currentAmountInCents -= 10;
        } else if (currentAmountInCents >= 5) {
            currentAmountInCents -= 5;
        } else if (currentAmountInCents >= 2) {
            currentAmountInCents -= 2;
        } else if (currentAmountInCents >= 1) {
            currentAmountInCents -= 1;
        }
        coinsCount++;
    }
    console.log(coinsCount);
}


// coins(["1.23"]);
// coins(["2.49"]);
// coins(["1.51"]);
