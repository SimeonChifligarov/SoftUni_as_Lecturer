function summerOutfit(input) {
    let degrees = Number(input[0]);
    let timeOfDay = input[1];

    let clothes;
    let shoes;

    if (timeOfDay == "Morning") {
        if (degrees >= 10 && degrees <= 18) {
            clothes = "Sweatshirt";
            shoes = "Sneakers";
        } else if (degrees > 18 && degrees <= 24) {
            clothes = "Shirt";
            shoes = "Moccasins";
        } else if (degrees >= 25) {
            clothes = "T-Shirt";
            shoes = "Sandals";
        }
    } else if (timeOfDay == "Afternoon") {
        if (degrees >= 10 && degrees <= 18) {
            clothes = "Shirt";
            shoes = "Moccasins";
        } else if (degrees > 18 && degrees <= 24) {
            clothes = "T-Shirt";
            shoes = "Sandals";
        } else if (degrees >= 25) {
            clothes = "Swim Suit";
            shoes = "Barefoot";
        }
    } else if (timeOfDay == "Evening") {
        if (degrees >= 10 && degrees <= 18) {
            clothes = "Shirt";
            shoes = "Moccasins";
        } else if (degrees > 18 && degrees <= 24) {
            clothes = "Shirt";
            shoes = "Moccasins";
        } else if (degrees >= 25) {
            clothes = "Shirt";
            shoes = "Moccasins";
        }
    }

    console.log(`It's ${degrees} degrees, get your ${clothes} and ${shoes}.`);
}

// summerOutfit(["16", "Morning"]);
