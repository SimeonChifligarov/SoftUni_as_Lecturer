function oscars(input) {
    let actorName = input[0];
    let actorPoints = Number(input[1]);
    let evaluatorsCount = Number(input[2]);

    for (let i = 0; i < evaluatorsCount * 2; i += 2) {
        let evaluatorName = input[i + 3];
        let evaluatorPoints = Number(input[i + 4]);

        actorPoints += evaluatorName.length * evaluatorPoints / 2;
        // console.log(actorPoints);
        if (actorPoints > 1250.50) {
            console.log(`Congratulations, ${actorName} got a nominee for leading role with ${actorPoints.toFixed(1)}!`);
            break;
        }
    }

    if (actorPoints <= 1250.50) {
        console.log(`Sorry, ${actorName} you need ${(1250.5 - actorPoints).toFixed(1)} more!`);
    }

}


// oscars(["Zahari Baharov",
//     "205",
//     "4",
//     "Johnny Depp",
//     "45",
//     "Will Smith",
//     "29",
//     "Jet Lee",
//     "10",
//     "Matthew Mcconaughey",
//     "39"]);
