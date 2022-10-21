function cinema(input) {
    let premierePrice = 12.00;
    let normalPrice = 7.50;
    let discountPrice = 5.00;

    let ticketType = input[0];
    let rows = Number(input[1]);
    let cols = Number(input[2]);

    let income = 0;

    if (ticketType == "Premiere") {
        income = rows * cols * premierePrice;
    } else if (ticketType == "Normal") {
        income = rows * cols * normalPrice;
    } else if (ticketType == "Discount") {
        income = rows * cols * discountPrice;
    }

    console.log(income.toFixed(2) + " leva");
}

// cinema(["Premiere", "10", "12"]);
