function toyShop(input) {
    let puzzleCost = 2.60;
    let dollCost = 3;
    let teddyBearCost = 4.10;
    let minionsCost = 8.20 ;
    let truckCost = 2;
 
    let vacationCost = Number(input[0]);
    let puzzleCount = Number(input[1]);
    let dollCount = Number(input[2]);
    let teddyBearsCount = Number(input[3]);
    let minionsCount = Number(input[4]);
    let trucksCount = Number(input[5]);
 
    let totalIncome = puzzleCost * puzzleCount + dollCost * dollCount 
        + teddyBearCost * teddyBearsCount + minionsCost * minionsCount + truckCost * trucksCount
 
    if ((puzzleCount + dollCount + teddyBearsCount + minionsCount + trucksCount) >= 50) {
        totalIncome *= 0.75;
    }
 
    totalIncome *= 0.90;
 
    if (totalIncome >= vacationCost) {
        console.log(`Yes! ${totalIncome - vacationCost} lv left.`);
    } else {
        console.log(`Not enough money! ${vacationCost - totalIncome} lv needed.`);
    }
}
 
 
toyShop(["40.8", "20", "25", "30", "50", "10"]);