function walking(input) {
    let targetSteps = 10000;
    let goingHomeCommand = "Going home";

    let sumSteps = 0;
    let i = 0;

    let currentAction = input[i];
    while (currentAction != goingHomeCommand) {
        let currentSteps = Number(currentAction);
        sumSteps += currentSteps;

        if (sumSteps >= targetSteps) {
            console.log("Goal reached! Good job!");
            console.log(`${sumSteps - targetSteps} steps over the goal!`);
        }

        i++;
        if (i >= input.length) {
            break;
        }
        currentAction = input[i];
    }

    if (currentAction == goingHomeCommand) {
        sumSteps += Number(input[i + 1]);
        if (sumSteps >= targetSteps) {
            console.log("Goal reached! Good job!");
            console.log(`${sumSteps - targetSteps} steps over the goal!`);
        } else {
            console.log(`${targetSteps - sumSteps} more steps to reach goal.`);
        }
    }

}


// walking([
//     "1000",
//     "1500",
//     "2000",
//     "6500",
// ]);

// walking([
//     "125",
//     "250",
//     "4000",
//     "30",
//     "2678",
//     "4682",  
// ]);
