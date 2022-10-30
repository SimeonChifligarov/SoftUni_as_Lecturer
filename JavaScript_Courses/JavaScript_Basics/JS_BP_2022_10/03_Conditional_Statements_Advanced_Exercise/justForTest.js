function fruitShop(input) {
    let type = input[0];
    let day = input[1];
    let quanity = Number(input[2]);
    let finalPrice = 0;
    if (day === "Monday" || day === "Tuesday" || day === "Wednesday" || day === "Thursday" || day === "Friday") {
        switch (type) {
            case "banana": console.log((finalPrice = quanity * 2.50).toFixed(2)); break;
            case "apple": console.log((finalPrice = quanity * 1.20).toFixed(2)); break;
            case "orange": console.log((finalPrice = quanity * 0.85).toFixed(2)); break;
            case "grapefruit": console.log((finalPrice = quanity * 1.45).toFixed(2)); break;
            case "kiwi": console.log((finalPrice = quanity * 2.70).toFixed(2)); break;
            case "pineapple": console.log((finalPrice = quanity * 5.50).toFixed(2)); break;
            case "grapes": console.log((finalPrice = quanity * 3.85).toFixed(2)); break;
        }
    }

    else if (day === "Sunday" || day === "Saturday") {
        switch (type) {
            case "banana": console.log((finalPrice = quanity * 2.70).toFixed(2)); break;
            case "apple": console.log((finalPrice = quanity * 1.25).toFixed(2)); break;
            case "orange": console.log((finalPrice = quanity * 0.90).toFixed(2)); break;
            case "grapefruit": console.log((finalPrice = quanity * 1.60).toFixed(2)); break;
            case "kiwi": console.log((finalPrice = quanity * 3).toFixed(2)); break;
            case "pineapple": console.log((finalPrice = quanity * 5.60).toFixed(2)); break;
            case "grapes": console.log((finalPrice = quanity * 4.20).toFixed(2)); break;

        }

    }


}
fruitShop(["tomato",
    "Friday",
    "2"])