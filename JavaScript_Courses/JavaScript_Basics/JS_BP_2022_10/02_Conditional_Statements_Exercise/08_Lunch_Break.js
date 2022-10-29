function lunchBreak(input) {
    let showName = input[0];  // "Game of Thrones"
    let showDuration = Number(input[1]);  // 60
    let breakDuration = Number(input[2]);  // 96

    let lunchDuration = breakDuration / 8;
    let restingDuration = breakDuration / 4;

    let usedTime = lunchDuration + restingDuration;
    // breakDuration -= lunchDuration;
    // breakDuration -= restingDuration;

    if ((breakDuration - usedTime) >= showDuration) {
        console.log(`You have enough time to watch ${showName} and left with ${Math.ceil(breakDuration - showDuration)} minutes free time.`);
    } else {
        console.log(`You don't have enough time to watch ${showName}, you need ${Math.ceil(showDuration - breakDuration)} more minutes.`);
    }


}

// lunchBreak(["Game of Thrones", "60", "96"]);
// lunchBreak(["Teen Wolf", "48", "60"]);

