function sumOfNumbers(input) {
    let numberAsText = input[0];

    let sum = 0;
    for (let i = 0; i < numberAsText.length; i++) {
        let currentNumber = Number(numberAsText[i]);
        sum += currentNumber;
    }

    console.log(`The sum of the digits is:${sum}`);
}

// sumOfNumbers(["564891"]);
