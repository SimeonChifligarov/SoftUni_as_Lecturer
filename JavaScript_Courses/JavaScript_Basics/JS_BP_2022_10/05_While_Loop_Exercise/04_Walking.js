function walking(input) {
    let goalSteps = 10000;
    let realSteps = 0;

    let i = 0;
    while (true) {
        let currentCommand = input[i];
        i++;

        if (currentCommand == "Going home") {
            let currentStepsGoingHome = Number(input[i]);
            realSteps += currentStepsGoingHome;
            if (realSteps < goalSteps) {
                console.log(`${goalSteps - realSteps} more steps to reach goal.`);
            } else {
                console.log('Goal reached! Good job!');
                console.log(`${realSteps - goalSteps} steps over the goal!`);
            }
            break;
        }

        let currentSteps = Number(currentCommand);
        realSteps += currentSteps;  // realSteps += Number(currentCommand) instead of line 15 & 16

        if (realSteps >= goalSteps) {
            console.log('Goal reached! Good job!');
            console.log(`${realSteps - goalSteps} steps over the goal!`);
            break;
        }
    }

}


walking(["1000",
    "1500",
    "2000",
    "6500"]);
