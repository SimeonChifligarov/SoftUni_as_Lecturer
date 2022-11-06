function equalSumsEvenOddPosition(input) {  // ["100000", "100050"]
    let intervalStart = Number(input[0]);
    let intervalEnd = Number(input[1]);

    let result = '';

    for (let num = intervalStart; num <= intervalEnd; num++) {
        let evenSum = 0;
        let oddSum = 0;

        let numAsString = String(num);  // "100000"
        // for (let i = 0; i < 6; i++) {
        for (let i = 0; i < numAsString.length; i++) {
            let currentDigit = numAsString[i];
            let currentDigitAsNumber = Number(currentDigit);
            if (i % 2 == 0) {
                evenSum += currentDigitAsNumber;
            } else {
                oddSum += currentDigitAsNumber;
            }
        }

        if (evenSum == oddSum) {
            result += `${numAsString} `;
        }
    }

    console.log(result);
}


// equalSumsEvenOddPosition(["100000", "100050"]);
