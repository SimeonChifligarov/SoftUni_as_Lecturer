function tennisRanklist(input) {
    let pointsW = 2000;
    let pointsF = 1200;
    let pointsSF = 720;

    let tournamentsCount = Number(input[0]);
    let startingPoints = Number(input[1]);

    let totalPoints = startingPoints;
    let tournamentsW = 0;


    for (let i = 2; i < input.length; i++) {
        let currentResult = input[i];

        if (currentResult == "W") {
            totalPoints += pointsW;
            tournamentsW++;
        } else if (currentResult == "F") {
            totalPoints += pointsF;
        } else if (currentResult == "SF") {
            totalPoints += pointsSF;
        }
    }

    console.log(`Final points: ${totalPoints}`);
    console.log(`Average points: ${Math.floor((totalPoints - startingPoints) / tournamentsCount)}`);
    console.log(`${(tournamentsW / tournamentsCount * 100).toFixed(2)}%`);
}


// tennisRanklist(["5",
//     "1400",
//     "F",
//     "SF",
//     "W",
//     "W",
//     "SF"]);
