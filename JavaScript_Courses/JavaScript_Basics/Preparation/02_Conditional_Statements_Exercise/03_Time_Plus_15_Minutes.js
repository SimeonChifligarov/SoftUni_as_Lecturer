function timePlus15Minutes(input) {
    let hour = Number(input[0]);
    let minutes = Number(input[1]);

    let newHour = hour;
    let newMinutes = minutes + 15;
    if (newMinutes >= 60) {
        newMinutes -= 60;
        newHour += 1;
        if (newHour == 24) {
            newHour = 0;
        }
    }

    if (newMinutes < 10) {
        console.log(`${newHour}:0${newMinutes}`);
    } else {
        console.log(`${newHour}:${newMinutes}`);
    }
}

// timePlus15Minutes(["1", "46"]);
// timePlus15Minutes(["23", "59"]);
