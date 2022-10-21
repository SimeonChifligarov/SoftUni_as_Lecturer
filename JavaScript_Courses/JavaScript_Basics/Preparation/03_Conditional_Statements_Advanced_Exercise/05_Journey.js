function journey(input) {
    // •	Втори–  Един от двата възможни сезона: "summer" или "winter"
    let budget = Number(input[0]);
    let season = input[1];

    let destination;
    let vacationType;
    let costAsPercent = 0;

    if (budget <= 100) {
        destination = "Bulgaria";
        if (season == "summer") {
            vacationType = "Camp";
            costAsPercent = 0.30;
        } else if (season == "winter") {
            vacationType = "Hotel";
            costAsPercent = 0.70;
        }
    } else if (budget <= 1000) {
        destination = "Balkans";
        if (season == "summer") {
            vacationType = "Camp";
            costAsPercent = 0.40;
        } else if (season == "winter") {
            vacationType = "Hotel";
            costAsPercent = 0.80;
        }
    } else {
        destination = "Europe";
        vacationType = "Hotel";
        costAsPercent = 0.90;
    }

    console.log(`Somewhere in ${destination}`);
    console.log(`${vacationType} - ${(budget * costAsPercent).toFixed(2)}`);
}

// journey(["75", "winter"]);
