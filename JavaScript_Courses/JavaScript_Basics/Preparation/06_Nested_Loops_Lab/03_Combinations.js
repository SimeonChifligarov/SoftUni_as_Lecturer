function combinations(input) {
    let targetNumber = Number(input[0]);

    let validCombinationsCount = 0;

    for (let x1 = 0; x1 <= targetNumber; x1++) {
        for (let x2 = 0; x2 <= targetNumber; x2++) {
            for (let x3 = 0; x3 <= targetNumber; x3++) {
                let currentSum = x1 + x2 + x3;
                if (currentSum == targetNumber) {
                    validCombinationsCount++;
                }
            }
        }
    }

    console.log(validCombinationsCount);
}


// combinations(["25"]);
