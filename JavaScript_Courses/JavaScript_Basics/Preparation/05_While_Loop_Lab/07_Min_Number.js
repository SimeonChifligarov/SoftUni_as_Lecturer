function minNumber(input) {
    let currentMin = Number(input[0]);

    let i = 1;
    while (true) {
        let currentCommand = input[i];
        i++;

        if (currentCommand == "Stop") {
            break;
        }

        if (Number(currentCommand) < currentMin) {
            currentMin = Number(currentCommand);
        }
    }

    console.log(currentMin);
}


// minNumber(["100",
//     "99",
//     "80",
//     "70",
//     "Stop"]);
