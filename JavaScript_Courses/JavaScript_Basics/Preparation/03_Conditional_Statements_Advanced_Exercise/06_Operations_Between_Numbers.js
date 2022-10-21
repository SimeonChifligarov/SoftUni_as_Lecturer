function operationsBetweenNumbers(input) {
    let num1 = Number(input[0]);
    let num2 = Number(input[1]);
    let operator = input[2];

    let result = 0;
    let result_as_string;

    if (operator == "+") {
        result = num1 + num2;
        let evenOrOdd;

        if (result % 2 == 0) {
            evenOrOdd = "even";
        } else {
            evenOrOdd = "odd";
        }

        result_as_string = `${num1} ${operator} ${num2} = ${result} - ${evenOrOdd}`;

    } else if (operator == "-") {
        result = num1 - num2;
        let evenOrOdd;

        if (result % 2 == 0) {
            evenOrOdd = "even";
        } else {
            evenOrOdd = "odd";
        }

        result_as_string = `${num1} ${operator} ${num2} = ${result} - ${evenOrOdd}`;

    } else if (operator == "*") {
        result = num1 * num2;
        let evenOrOdd;

        if (result % 2 == 0) {
            evenOrOdd = "even";
        } else {
            evenOrOdd = "odd";
        }

        result_as_string = `${num1} ${operator} ${num2} = ${result} - ${evenOrOdd}`;
        
    } else if (operator == "/") {
        if (num2 == 0) {
            result_as_string = `Cannot divide ${num1} by zero`;
        } else {
            result = num1 / num2;
            result_as_string = `${num1} ${operator} ${num2} = ${result.toFixed(2)}`;
        }

    } else if (operator == "%") {
        if (num2 == 0) {
            result_as_string = `Cannot divide ${num1} by zero`;
        } else {
            result = num1 % num2;
            result_as_string = `${num1} ${operator} ${num2} = ${result}`;
        }
        
    }

    console.log(result_as_string);
}

// operationsBetweenNumbers(["10", "12", "+"]);
