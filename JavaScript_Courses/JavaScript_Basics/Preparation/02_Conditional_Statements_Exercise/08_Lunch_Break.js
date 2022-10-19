function lunchBreak(input) {
    let show = input[0];
    let showDuration = Number(input[1]);
    let breakDuration = Number(input[2]);

    let lunchTime = breakDuration / 8;
    let restTime = breakDuration / 4;

    breakDuration -= lunchTime + restTime;

    if (breakDuration >= showDuration) {
        console.log(`You have enough time to watch ${show} and left with ${Math.ceil(breakDuration - showDuration)} minutes free time.`);
    } else {
        console.log(`You don't have enough time to watch ${show}, you need ${Math.ceil(showDuration - breakDuration)} more minutes.`);
    }
}

// lunchBreak(["Teen Wolf", "48", "60"]);
