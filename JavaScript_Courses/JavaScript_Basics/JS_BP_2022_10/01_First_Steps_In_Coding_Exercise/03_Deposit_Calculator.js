function depositCalculator(input) {
    let depositAmount = Number(input[0]);  // 200  // "200"
    let depositMonths = Number(input[1]); // 3
    let annualInterestRate222 = Number(input[2]) / 100;  // 0.057

    let finalAmount = depositAmount + depositMonths * ((depositAmount * annualInterestRate222) / 12);

    console.log(finalAmount);
}

// depositCalculator(["200", "3", "5.7"]);
