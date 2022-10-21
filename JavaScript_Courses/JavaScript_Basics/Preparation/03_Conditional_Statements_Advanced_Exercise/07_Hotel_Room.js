function hotelRoom(input) {
    let month = input[0];
    let nights = Number(input[1]);

    let studioNight = 0;
    let apartamentNight = 0;

    let studioDiscount = 0;
    let apartamentDiscount = 0;

    if (nights > 14) {
        apartamentDiscount = 0.10;
    }

    if (month == "May" || month == "October") {
        studioNight = 50;
        apartamentNight = 65;
        if (nights > 7 && nights <= 14) {
            studioDiscount = 0.05;
        } else if (nights > 14) {
            studioDiscount = 0.30;
        }
    } else if (month == "June" || month == "September") {
        studioNight = 75.20;
        apartamentNight = 68.70;
        if (nights > 14) {
            studioDiscount = 0.20;
        } 
    } else if (month == "July" || month == "August") {
        studioNight = 76;
        apartamentNight = 77;
    }

    let apartamentTotal = apartamentNight * (1 - apartamentDiscount) * nights;
    let studioTotal = studioNight * (1 - studioDiscount) * nights;

    console.log(`Apartment: ${apartamentTotal.toFixed(2)} lv.`);
    console.log(`Studio: ${studioTotal.toFixed(2)} lv.`);
}

// hotelRoom(["May", "15"]);
