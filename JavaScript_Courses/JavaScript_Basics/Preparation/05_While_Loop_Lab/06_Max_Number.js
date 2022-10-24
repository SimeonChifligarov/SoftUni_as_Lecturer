function maxNumber(input) {
    let currentMax = Number(input[0]);

    let i = 1;
    while (true) {
        let currentCommand = input[i];
        i++;

        if (currentCommand == "Stop") {
            break;
        }

        if (Number(currentCommand) > currentMax) {
            currentMax = Number(currentCommand);
        }
    }

    console.log(currentMax);
}


// maxNumber(["100",
//     "99",
//     "80",
//     "70",
//     "Stop"]);
