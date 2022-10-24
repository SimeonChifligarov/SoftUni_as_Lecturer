function graduation(input) {
    // ако годишната му оценка е по-голяма или равна на 4.00. 
    // Ако ученикът бъде скъсан повече от един път, то той бива 
    // изключен и програмата приключва, като се отпечатва името на ученика и в кой клас бива изключен.
    let student = input[0];
    let fails = 0;
    let currentGrade = 1;
    let totalScore = 0;

    let i = 1;
    while (true) {
        if (currentGrade > 12) {
            console.log(`${student} graduated. Average grade: ${(totalScore/12).toFixed(2)}`);
            break;
        }

        let currentScore = Number(input[i]);
        i++;

        if (currentScore < 4) {
            fails += 1;
            if (fails == 2) {
                console.log(`${student} has been excluded at ${currentGrade} grade`);
                break;
            }
        } else {
            totalScore += currentScore;
            currentGrade++;
        }

    }
}


// graduation(["Gosho",
//     "5",
//     "5.5",
//     "6",
//     "5.43",
//     "5.5",
//     "6",
//     "5.55",
//     "5",
//     "6",
//     "6",
//     "5.43",
//     "5"]);
