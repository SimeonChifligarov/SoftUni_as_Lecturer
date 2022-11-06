function trainTheTrainers(input) {  // ["3","Arrays","4.53","5.23","5.00","Lists","5.83","6.00","5.42","Finish"]
    let judgesCount = Number(input[0]);
    let totalGradeSum = 0;
    let totalPresentationsCount = 0;
    // comment
    let i = 1;
    let currentPresentation = input[i];  // comment...
    i++;

    while (currentPresentation != "Finish") {
        totalPresentationsCount++;

        let presentationGrade = 0;
        for (let j = 0; j < judgesCount; j++) {
            let currentGrade = Number(input[i]);
            i++;

            presentationGrade += currentGrade;
            totalGradeSum += currentGrade;
        }

        console.log(`${currentPresentation} - ${(presentationGrade / judgesCount)}.`);

        currentPresentation = input[i];
        i++;

        // current               (i - 1)
    }


    console.log(`Student's final assessment is ${(totalGradeSum / (totalPresentationsCount * judgesCount))}.`);

}


// trainTheTrainers(["2",
//     "While-Loop",
//     "6.00",
//     "5.50",
//     "For-Loop",
//     "5.84",
//     "5.66",
//     "Finish"]);

// trainTheTrainers(["3",
//     "Finish"]);