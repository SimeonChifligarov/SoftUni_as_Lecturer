function moving(input) {
    let width = Number(input[0]);
    let length = Number(input[1]);
    let heigth = Number(input[2]);

    let spaceAvailable = width * length * heigth;
    let i = 3;

    while (true) {
        let currentCommand = input[i];
        
        if (currentCommand == "Done") {
            console.log(`${spaceAvailable} Cubic meters left.`);
            break;
        }

        let currentSpace = Number(currentCommand);
        spaceAvailable -= currentSpace;

        if (spaceAvailable < 0) {
            console.log(`No more free space! You need ${-spaceAvailable} Cubic meters more.`);
            break;
        }

        i++;
    }
}


// moving([
//     "10",
//     "10",
//     "2",
//     "20",
//     "20",
//     "20",
//     "20",
//     "122",
// ]);
