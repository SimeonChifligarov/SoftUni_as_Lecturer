function cinema(input) {
    let premierePrice = 12.00;
    let normalPrice = 7.50;
    let discountPrice = 5.00;

    let ticketType = input[0];
    let rows = Number(input[1]);  // 10 Number
    let cols = Number(input[2]);  // 12 Number

    // let income = 0;
    let ticketPrice = 0;

    if (ticketType == "Premiere") {
        ticketPrice = premierePrice;
    } else if (ticketType == "Normal") {
        ticketPrice = normalPrice;
    } else if (ticketType == "Discount") {
        ticketPrice = discountPrice;
    }

    let income = rows * cols * ticketPrice;

    console.log(`${income.toFixed(2)} leva`);  // `
}

// cinema(["Premiere", "10", "12"]);
