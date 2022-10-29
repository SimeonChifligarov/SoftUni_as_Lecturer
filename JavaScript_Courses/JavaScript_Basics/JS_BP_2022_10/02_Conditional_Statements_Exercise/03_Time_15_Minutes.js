function time15Minutes(input) {
    let hours = Number(input[0]);  // 1
    let minutes = Number(input[1]);

    let minutesPlus15 = minutes + 15;

    // console.log(minutesPlus15);

    if (minutesPlus15 >= 60) {
        hours += 1;  // hours = hours + 1;
        minutesPlus15 -= 60;  // minutesPlus15 = minutesPlus15 - 60;
    }

    if (hours == 24) {  // 0, 1, ... 23; 24 => 0
        hours = 0;
    }

    if (minutesPlus15 < 10) {  // (minutesPlus15 <= 9)
        console.log(`${hours}:0${minutesPlus15}`);  // 0, 1, 2,... 9
    } else {
        console.log(`${hours}:${minutesPlus15}`);
    }

}

// time15Minutes(["1", "46"]);
// time15Minutes(["23", "55"]);
