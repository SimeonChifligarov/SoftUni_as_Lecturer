function skiTrip(input) {
    let nights = Number(input[0]) - 1;
    let space = input[1];
    let valuation = input[2];

    let totalCost = 0;

    if (space == "room for one person") {
        totalCost = nights * 18;
    } else if (space == "apartment") {
        totalCost = nights * 25;
        if (nights < 10) {
            totalCost *= 0.70;
        } else if (nights <= 15) {
            totalCost *= 0.65;
        } else {
            totalCost *= 0.50;
        }
    } else if (space == "president apartment") {
        totalCost = nights * 35;
        if (nights < 10) {
            totalCost *= 0.90;
        } else if (nights <= 15) {
            totalCost *= 0.85;
        } else {
            totalCost *= 0.80;
        }
    }

    if (valuation == "positive") {
        totalCost *= 1.25;
    } else if (valuation == "negative") {
        totalCost *= 0.90;
    }

    console.log(`${totalCost.toFixed(2)}`);
}

// skiTrip(["14", "apartment", "positive"]);
