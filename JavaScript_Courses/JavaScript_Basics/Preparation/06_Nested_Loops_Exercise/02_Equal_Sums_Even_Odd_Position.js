function equalSumsEvenOddPosition(input) {
    let intervalStart = Number(input[0]);
    let intervalEnd = Number(input[1]);

    let result = '';

    for (let num = intervalStart; num <= intervalEnd; num++) {
        let evenSum = 0;
        let oddSum = 0;

        let numAsString = String(num);
        // for (let i = 0; i < 6; i++) {
        for (let i = 0; i < numAsString.length; i++) {
            if (i % 2 == 0) {
                evenSum += Number(numAsString[i]);
            } else {
                oddSum += Number(numAsString[i]);
            }
        }

        if (evenSum == oddSum) {
            result += `${numAsString} `;
        }
    }

    console.log(result);
}


// equalSumsEvenOddPosition(["100000", "100050"]);
