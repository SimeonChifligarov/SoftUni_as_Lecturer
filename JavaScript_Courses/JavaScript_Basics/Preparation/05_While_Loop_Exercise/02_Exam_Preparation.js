function examPreparation(input) {
    let limitBadGrades = Number(input[0]);
    let i = 1;

    let currentBadGrades = 0;
    let sumScore = 0;
    let problemsCount = 0;
    let lastProblem = "";

    while (true) {
        let currentTask = input[i];
        let currentGrade = Number(input[i + 1]);


        if (currentTask == "Enough") {
            console.log(`Average score: ${(sumScore / problemsCount).toFixed(2)}`);
            console.log(`Number of problems: ${problemsCount}`);
            console.log(`Last problem: ${lastProblem}`);
            break;
        }

        if (currentGrade <= 4) {
            currentBadGrades++;
            if (currentBadGrades == limitBadGrades) {
                console.log(`You need a break, ${currentBadGrades} poor grades.`);
                break;
            }
        }

        lastProblem = currentTask;
        problemsCount++;
        sumScore += currentGrade;
        i += 2;
    }

}


// examPreparation([
//     "3",
//     "Money",
//     "6",
//     "Story",
//     "4",
//     "Spring Time",
//     "5",
//     "Bus",
//     "6",
//     "Enough"
// ]);


// examPreparation([
//     "2",
//     "Income",
//     "3",
//     "Game Info",
//     "6",
//     "Best Player",
//     "4"
// ]);
