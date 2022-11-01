function cakeNew(input) {
    let width = Number(input[0]);
    let length = Number(input[1]);

    let totalPieces = width * length;
    let leftPieces = totalPieces;

    let i = 2;
    let currentCommand = input[i];
    i++;

    while (currentCommand != "STOP") {
        let currentCakes = Number(currentCommand);
        leftPieces -= currentCakes;

        if (leftPieces < 0) {
            console.log(`No more cake left! You need ${-leftPieces} pieces more.`);
            break;
        }

        currentCommand = input[i];
        i++;
    }

    if (currentCommand == "STOP") {
        console.log(`${leftPieces} pieces are left.`);
    }
}


cakeNew(["10",
"2",
"2",
"4",
"6",
"STOP"]);

