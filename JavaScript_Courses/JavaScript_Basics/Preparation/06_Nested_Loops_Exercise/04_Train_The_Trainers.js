function trainTheTrainers(input) {
    // броят на хората в журито n - цяло число в интервала [1…20]
    let juryCount = Number(input[0]);

    let totalSum = 0;
    let totalPresentations = 0;

    let i = 1;

    while (true) {
        let currentPresentation = input[i];

        if (currentPresentation == "Finish") {
            break;
        }

        totalPresentations++;
        let currentSum = 0;

        for (j = 0; j < juryCount; j++) {
            i++;
            currentSum += Number(input[i]);
            totalSum += Number(input[i]);
        }

        console.log(`${currentPresentation} - ${(currentSum / juryCount).toFixed(2)}.`);
        i++;
    }

    console.log(`Student's final assessment is ${(totalSum / (juryCount * totalPresentations)).toFixed(2)}.`);
}


// trainTheTrainers([
//     "2",
//     "While-Loop",
//     "6.00",
//     "5.50",
//     "For-Loop",
//     "5.84",
//     "5.66",
//     "Finish",
// ]);
