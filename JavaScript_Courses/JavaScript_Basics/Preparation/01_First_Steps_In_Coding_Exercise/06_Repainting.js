function repainting(input) {
    let plastic = Number(input[0]) + 2;
    let paint = Number(input[1]) * 1.10;
    let diluent = Number(input[2]);
    let workHours = Number(input[3]);

    let bagsSum = 0.40;

    let totalSum = plastic * 1.50 + paint * 14.50 + diluent * 5.00 + bagsSum;
    let workerSum = totalSum * 0.30 * workHours;

    let result = totalSum + workerSum;

    console.log(result);
}

// repainting(["10 ", "11 ", "4 ", "8 "]);
// repainting(["5 ", "10 ", "10 ", "1 "]);
