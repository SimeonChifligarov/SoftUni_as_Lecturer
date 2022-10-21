function onTimeForTheExam(input) {
    let hourExam = Number(input[0]);
    let minuteExam = Number(input[1]);
    let hourArrival = Number(input[2]);
    let minuteArrival = Number(input[3]);

    let examTimeAsMinutes = hourExam * 60 + minuteExam;
    let arrivalTimeAsMinutes = hourArrival * 60 + minuteArrival;

    let diff = arrivalTimeAsMinutes - examTimeAsMinutes;
    if (diff > 0) {
        console.log('Late');
        if (diff < 60) {
            console.log(`${(diff)} minutes after the start`);
        } else {
            let diffHours = Math.floor(diff / 60);
            let diffMins = diff % 60;
            if (diffMins < 10) {
                diffMins = `0${diffMins}`;
            }
            console.log(`${diffHours}:${diffMins} hours after the start`);
        }
    } else if (diff >= - 30) {
        console.log('On time');
        if (diff != 0) {
            console.log(`${(-diff)} minutes before the start`);
        }
    } else {
        console.log('Early');
        if (diff > -60) {
            console.log(`${(-diff)} minutes before the start`);
        } else {
            let diffHours = Math.floor((-diff) / 60);
            let diffMins = (-diff) % 60;
            if (diffMins < 10) {
                diffMins = `0${diffMins}`;
            }
            console.log(`${diffHours}:${diffMins} hours before the start`);
        }
    }

}


// onTimeForTheExam(["9", "30", "9", "50"]);
// onTimeForTheExam(["11", "30", "10", "55"]);
