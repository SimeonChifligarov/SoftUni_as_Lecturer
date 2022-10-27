function specialNumbers(input) {
    let num = Number(input[0]);

    let result = '';

    for (let currentNum = 1111; currentNum <= 9999; currentNum++) {
        let currentNumAsString = String(currentNum);
        let isValid = true;

        for (i = 0; i < currentNumAsString.length; i++) {
            let currentDigit = Number(currentNumAsString[i]);

            if (num % currentDigit != 0) {
                isValid = false;
                break;
            }
        }

        if (isValid) {
            result += `${currentNumAsString} `;
        }
    }

    console.log(result);
}


// specialNumbers(["3"]);
