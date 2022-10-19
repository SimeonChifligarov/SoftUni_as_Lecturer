function toyShop(input) {
    // let puzzlePrice = 2.60;
    // let speakingDollPrice = 3;
    // let teddyBearPrice = 4.10;
    // let minionPrice = 8.20;
    // let toyCarPrice = 2;

    let vacationPrice = Number(input[0]);
    let puzzleCount = Number(input[1]);
    let speakingDollCount = Number(input[2]);
    let teddyBearCount = Number(input[3]);
    let minionCount = Number(input[4]);
    let toyCarCount = Number(input[5]);

    let totalSum = 2.6 * puzzleCount + 3 * speakingDollCount + 4.1 * teddyBearCount + 8.2 * minionCount + 2 * toyCarCount;

    let totalCount = puzzleCount + speakingDollCount + teddyBearCount + minionCount + toyCarCount;

    if (totalCount >= 50) {
        totalSum *= 0.75;

        // let discount = totalSum * 0.25;
        // totalSum -= discount;
    }

    totalSum *= 0.90;

    let difference = totalSum - vacationPrice;

    if (difference >= 0) {
        console.log(`Yes! ${difference.toFixed(2)} lv left.`);
    } else {
        console.log(`Not enough money! ${-difference.toFixed(2)} lv needed.`);
    }
}

// toyShop(["40.8", "20", "25", "30", "50", "10"]);
// toyShop(["320", "8", "2", "5", "5", "1"]);
