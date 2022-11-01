function coins(input) {
    // 2 лева, 1 лев, 50 стотинки, 20 стотинки, 10 стотинки, 5 стотинки, 2 стотинки или 1 стотинка 
    let moneyAmount = Number(input[0]);
    let coinsCount = 0;

    let currentAmountInCents = Math.round(moneyAmount * 100);
    // let currentAmountInCents = moneyAmount * 100;
    // console.log(currentAmountInCents);

    while (currentAmountInCents > 0) {  // while (cond1) {}
        coinsCount++;

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
    }
    console.log(coinsCount);
}


// coins(["1.23"]);
// coins(["2.49"]);
// coins(["1.51"]);
