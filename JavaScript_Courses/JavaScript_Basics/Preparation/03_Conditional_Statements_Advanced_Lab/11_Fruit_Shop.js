function fruitShop(input) {
    let fruit = input[0];
    let day = input[1];
    let quantity = Number(input[2]);

    let fruitPrice = 0;

    if (day == "Monday" || day == "Tuesday" || day == "Wednesday" || day == "Thursday" || day == "Friday") {
        if (fruit == "banana") {
            fruitPrice = 2.50;
        } else if (fruit == "apple") {
            fruitPrice = 1.20;
        } else if (fruit == "orange") {
            fruitPrice = 0.85;
        } else if (fruit == "grapefruit") {
            fruitPrice = 1.45;
        } else if (fruit == "kiwi") {
            fruitPrice = 2.70;
        } else if (fruit == "pineapple") {
            fruitPrice = 5.50;
        } else if (fruit == "grapes") {
            fruitPrice = 3.85;
        } else {
            console.log("error");
        }

    } else if (day == "Saturday" || day == "Sunday") {
        if (fruit == "banana") {
            fruitPrice = 2.70;
        } else if (fruit == "apple") {
            fruitPrice = 1.25;
        } else if (fruit == "orange") {
            fruitPrice = 0.90;
        } else if (fruit == "grapefruit") {
            fruitPrice = 1.60;
        } else if (fruit == "kiwi") {
            fruitPrice = 3.00;
        } else if (fruit == "pineapple") {
            fruitPrice = 5.60;
        } else if (fruit == "grapes") {
            fruitPrice = 4.20;
        } else {
            console.log("error");
        }
    } else {
        console.log("error");
    }

    if (fruitPrice != 0) {
        console.log((quantity * fruitPrice).toFixed(2));
    }
}

// fruitShop(["apple", "Tuesday", "2"]);
