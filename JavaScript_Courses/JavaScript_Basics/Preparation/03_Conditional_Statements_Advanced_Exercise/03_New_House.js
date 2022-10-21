function newHouse(input) {
    let rosePrice = 5;
    let dahliasPrice = 3.80;
    let tulipPrice = 2.80;
    let narcissusPrice = 3;
    let gladiolusPrice = 2.50;

    let flowersType = input[0];
    let flowersCount = Number(input[1]);
    let budget = Number(input[2]);

    let totalCost = 0;
    if (flowersType == "Roses") {
        totalCost = flowersCount * rosePrice;
        if (flowersCount > 80) {
            totalCost *= 0.90;
        }
    } else if (flowersType == "Dahlias") {
        totalCost = flowersCount * dahliasPrice;
        if (flowersCount > 90) {
            totalCost *= 0.85;
        }
    } else if (flowersType == "Tulips") {
        totalCost = flowersCount * tulipPrice;
        if (flowersCount > 80) {
            totalCost *= 0.85;
        }
    } else if (flowersType == "Narcissus") {
        totalCost = flowersCount * narcissusPrice;
        if (flowersCount < 120) {
            totalCost *= 1.15;
        }
    } else if (flowersType == "Gladiolus") {
        totalCost = flowersCount * gladiolusPrice;
        if (flowersCount < 80) {
            totalCost *= 1.20;
        }
    }

    if (budget >= totalCost) {
        console.log(`Hey, you have a great garden with ${flowersCount} ${flowersType} and ${(budget - totalCost).toFixed(2)} leva left.`);
    } else {
        console.log(`Not enough money, you need ${(totalCost - budget).toFixed(2)} leva more.`);
    }
}

// newHouse(["Roses", "55", "250"]);
