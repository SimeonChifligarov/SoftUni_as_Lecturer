function sumNumbers(input) {
    let targetNum = Number(input[0]);

    let currentSum = 0;

    let i = 1;
    while (currentSum < targetNum) {
        currentSum += Number(input[i]);
        i++;
    }
    console.log(currentSum);
}


// sumNumbers(["100", "10", "20", "30", "40"]);
