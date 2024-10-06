function toyShop(input) {
    
    let puzzleCost = 2.60;
    let dollCost = 3;
    let teddyBearCost = 4.10;
    let minionCost = 8.20;
    let carCost = 2;

    let vacationCost = Number(input[0]);
    let puzzleCount = Number(input[1]);
    let dollCount = Number(input[2]);
    let teddyBearsCount = Number(input[3]);
    let minionsCount = Number(input[4]);
    let carsCount = Number(input[5]);

    let totalCount = puzzleCount + dollCount + teddyBearsCount + minionsCount + carsCount;

    let totalIncome = puzzleCost * puzzleCount + dollCost * dollCount
        + teddyBearCost * teddyBearsCount + minionCost * minionsCount + carCost * carsCount;

    if (totalCount >= 50) {
        totalIncome *= 0.75;

        // let discount = totalIncome * 0.25;
        // totalIncome -= discount;
    }

    totalIncome *= 0.90;

    if (totalIncome >= vacationCost) {
        console.log(`Yes! ${(totalIncome - vacationCost).toFixed(2)} lv left.`);
    } else {
        console.log(`Not enough money! ${(vacationCost - totalIncome).toFixed(2)} lv needed.`);
    }

}

// toyShop(["40.8", "20", "25", "30", "50", "10"]);
// toyShop(["320", "8", "2", "5", "5", "1"]);
