function sumSeconds(input) {
    let secondsFirst = Number(input[0]);
    let secondsSecond = Number(input[1]);
    let secondsThird = Number(input[2]);

    let sumSeconds = secondsFirst + secondsSecond + secondsThird;
    let minutes = Math.floor(sumSeconds / 60);
    let seconds = sumSeconds % 60;

    if (seconds < 10) {
        console.log(`${minutes}:0${seconds}`);
    } else {
        console.log(`${minutes}:${seconds}`);
    }
}

// sumSeconds(["35", "45", "44"]);
