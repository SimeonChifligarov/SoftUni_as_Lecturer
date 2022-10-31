function tennisRanklist(input) {
    //     Има три варианта за завършване на турнир:
    // W - ако е победител получава 2000 точки  // winner
    // F - ако е финалист получава 1200 точки   // final
    // SF - ако е полуфиналист получава 720 точки  // semi-final
    let startingPoints = Number(input[1]);
    let totalPointsGained = startingPoints;
    let countsW = Number(input[0]);
    let countsW = 0;

    countsW++;

    // •	"Final points: {брой точки след изиграните турнири}"
    // •	"Average points: {средно колко точки печели за турнир}"
    // •	"{процент спечелени турнири}%"

    console.log(`Final points: ${totalPoints}`);
    console.log(`Average points: ${averagePoints}`);  // averagePoints = totalPointsGained / tournamentCounts;
    // totalPointsGained = totalPoints - startingPoints  // input[1]
    console.log(`${percentTourWins}%`);  // percentTourWins = countsW / countsTotal;
}


tennisRanklist([
    "5",
    "1400",
    "F",
    "SF",
    "W",
    "W",
    "SF",
]);
