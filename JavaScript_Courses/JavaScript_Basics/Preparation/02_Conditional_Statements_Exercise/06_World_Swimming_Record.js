function worldSwimmingRecord(input) {
    let timeLostPer15Meters = 12.5;

    let recordTime = Number(input[0]);
    let meters = Number(input[1]);
    let secondsPerMeter = Number(input[2]);

    let numberOfLosts = Math.floor(meters / 15);
    let lostTime = numberOfLosts * timeLostPer15Meters;

    let totalTime = secondsPerMeter * meters + lostTime;

    if (totalTime < recordTime) {
        console.log(`Yes, he succeeded! The new world record is ${totalTime.toFixed(2)} seconds.`);
    } else {
        console.log(`No, he failed! He was ${(totalTime - recordTime).toFixed(2)} seconds slower.`);
    }
}

// worldSwimmingRecord(["10464", "1500", "20"]);
// worldSwimmingRecord(["55555.67", "3017", "5.03"]);
