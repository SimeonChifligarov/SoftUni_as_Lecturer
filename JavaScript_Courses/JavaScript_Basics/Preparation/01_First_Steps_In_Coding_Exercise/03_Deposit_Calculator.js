function depositCalculator(input) {
    let depositAmount = Number(input[0]);
    let depositTime = Number(input[1]);
    let interestRate = Number(input[2]) / 100;

    let depositAfter = depositAmount + depositTime * ((depositAmount * interestRate) / 12);

    console.log(depositAfter);
}

// depositCalculator(["200", "3", "5.7"]);
// depositCalculator(["2350", "6", "7"])
