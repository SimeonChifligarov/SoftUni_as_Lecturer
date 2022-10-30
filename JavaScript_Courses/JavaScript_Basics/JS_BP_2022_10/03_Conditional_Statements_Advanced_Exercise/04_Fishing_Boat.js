function fishingBoat(input) {
    let budget = Number(input[0]);
    let season = input[1];
    let fishermen = Number(input[2]);

    let totalCost = 0;


    if (season == "Spring") {
        totalCost = 3000;
    } else if (season == "Summer") {  // else if (season == "Summer" || season == "Autumn")
        totalCost = 4200;
    } else if (season == "Autumn") {
        totalCost = 4200;
    } else if (season == "Winter") {
        totalCost = 2600;
    }
    
    if (fishermen <= 6) {
        totalCost *= 0.90;
    } else if (fishermen <= 11) {
        totalCost *= 0.85;
    } else if (fishermen > 11) {   // >= 12
        totalCost *= 0.75;
    }

    if (fishermen % 2 == 0 && season != "Autumn") {
        totalCost *= 0.95;
    }

    if (budget >= totalCost) {
        // let diff = budget - totalCost;
        console.log(`Yes! You have ${(budget - totalCost).toFixed(2)} leva left.`);
    } else {
        console.log(`Not enough money! You need ${(totalCost - budget).toFixed(2)} leva.`);
    }
}


// fishingBoat(["3000", "Summer", "11"]);
