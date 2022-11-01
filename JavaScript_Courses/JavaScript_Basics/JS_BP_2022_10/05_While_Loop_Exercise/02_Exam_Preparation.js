function examPreparation(input) {  // ["3","Money","6","Story","4","Spring Time","5","Bus","6","Enough"]);
    // let exitMessage = "Enough";
    // let badGrade = 4;

    let badGradesLimit = Number(input[0]);
    let badGradesCurrent = 0;
    let totalTasks = 0;
    let sumTaks = 0;
    let lastProblemName = '';

    let i = 1;
    while (true) {
        let taskName = input[i];
        i++;

        if (taskName == "Enough") {  // taskName == "Enough"
            console.log(`Average score: ${(sumTaks / totalTasks).toFixed(2)}`);  // avg = (a1 + a2 + a2) / totalTasks 
            console.log(`Number of problems: ${totalTasks}`);
            console.log(`Last problem: ${lastProblemName}`);
            break;
        }


        let taskGrage = Number(input[i]);
        i++;


        totalTasks++;
        sumTaks += taskGrage;
        lastProblemName = taskName;

        if (taskGrage <= 4) {  // taskGrage <= 4
            badGradesCurrent++;
            if (badGradesCurrent == badGradesLimit) {
                console.log(`You need a break, ${badGradesCurrent} poor grades.`);
                break;
            }

        }
    }

}


// examPreparation(["3",
//     "Money",
//     "6",
//     "Story",
//     "4",
//     "Spring Time",
//     "5",
//     "Bus",
//     "6",
//     "Enough"]);

// examPreparation(["2",
//     "Income",
//     "3",
//     "Game Info",
//     "6",
//     "Best Player",
//     "4"]);
