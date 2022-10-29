function sumSeconds(input) {  // ["35", "45", "44"]
    let secondsFirst = Number(input[0]);  // 35
    let secondsSecond = Number(input[1]);
    let secondsThird = Number(input[2]);

    let secondsSum = secondsFirst + secondsSecond + secondsThird;

    let minutes = Math.floor(secondsSum / 60);
    let seconds = secondsSum % 60;

    // console.log(`${minutes}:${seconds}`);
    
    if (seconds < 10) {
    console.log(`${minutes}:0${seconds}`);
    } else {
    console.log(`${minutes}:${seconds}`);
    }
}

// sumSeconds(["35", "45", "44"]);
