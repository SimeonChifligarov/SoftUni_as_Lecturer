function cake(input) {
    let width = Number(input[0]);
    let length = Number(input[1]);

    let cakePieces = width * length;
    let leftPieces = cakePieces;


    let i = 2;
    while (true) {
        let currentCommand = input[i];
        i++;

        if (currentCommand == "STOP") {
            console.log(`${leftPieces} pieces are left.`);
            break;
        }

        let currentPieces = Number(currentCommand);
        leftPieces -= currentPieces;

        if (leftPieces < 0) {
            console.log(`No more cake left! You need ${-leftPieces} pieces more.`);  // Math.abs(leftPieces)
            break;
        }
    }
}


// cake(["10",
//     "10",
//     "20",
//     "20",
//     "20",
//     "20",
//     "21"]);

// cake(["10",
//     "2",
//     "2",
//     "4",
//     "6",
//     "STOP"]);
