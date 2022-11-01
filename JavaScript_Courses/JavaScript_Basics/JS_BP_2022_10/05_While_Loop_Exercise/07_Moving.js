function moving(input) {

    // 4.	На следващите редове (до получаване на команда "Done") - брой кашони, които се пренасят в квартирата - цели числа в интервала [1...10000];
    // Функцията трябва да приключи прочитането на данни при команда "Done" или ако свободното място свърши.

    let width = Number(input[0]);
    let length = Number(input[1]);
    let higth = Number(input[2]);

    let totalSpace = width * length * higth;
    let freeSpace = totalSpace;

    let i = 3;
    while (true) {
        let currentCommand = input[i];
        i++;

        if (currentCommand == "Done") {
            console.log(`${freeSpace} Cubic meters left.`);
            break;
        }

        let currentBoxes = Number(currentCommand);
        freeSpace -= currentBoxes;

        if (freeSpace < 0) {
            console.log(`No more free space! You need ${-freeSpace} Cubic meters more.`);  // Math.abs(freeSpace)
            break;
        }

    }

}


moving(["10",
    "10",
    "2",
    "20",
    "20",
    "20",
    "20",
    "122"]);