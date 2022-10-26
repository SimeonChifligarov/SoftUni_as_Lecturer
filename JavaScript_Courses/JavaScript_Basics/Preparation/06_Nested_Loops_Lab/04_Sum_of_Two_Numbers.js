function sumOfTwoNumbers(input) {
    let intervalStart = Number(input[0]);
    let intervalEnd = Number(input[1]);
    let magicNumber = Number(input[2]);

    let currentCombination = 0;
    let isFound = false;

    for (let n1 = intervalStart; n1 <= intervalEnd; n1++) {
        for (let n2 = intervalStart; n2 <= intervalEnd; n2++) {
            currentCombination++;

            currentSum = n1 + n2;

            if (currentSum == magicNumber) {
                console.log(`Combination N:${currentCombination} (${n1} + ${n2} = ${magicNumber})`);
                isFound = true;
                break;
            }
        }

        if (isFound) {
            break;
        }
    }

    // if (isFound === false) {
    if (!isFound) {
        console.log(`${currentCombination} combinations - neither equals ${magicNumber}`);
    }
}


// sumOfTwoNumbers(["1", "10", "5"]);
