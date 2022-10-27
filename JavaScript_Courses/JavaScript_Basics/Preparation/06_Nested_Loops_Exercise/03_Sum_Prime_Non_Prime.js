function sumPrimeNonPrime(input) {
    let sumPrime = 0;
    let sumNonPrime = 0;

    let i = 0;
    let currentCommand = input[i];

    while (currentCommand != "stop") {
        currentNum = Number(currentCommand);

        if (currentNum < 0) {
            console.log("Number is negative.");
            i++;
            currentCommand = input[i];
            continue;
        }

        let isPrime = true;
        for (let j = 2; j < currentNum; j++) {
            if (currentNum % j == 0) {
                isPrime = false;
                break;
            }
        }

        if (isPrime) {
            sumPrime += currentNum;
        } else {
            sumNonPrime += currentNum;
        }

        i++;
        currentCommand = input[i];
    }

    console.log(`Sum of all prime numbers is: ${sumPrime}`);
    console.log(`Sum of all non prime numbers is: ${sumNonPrime}`);
}


// sumPrimeNonPrime([
//     "3",
//     "9",
//     "0",
//     "7",
//     "19",
//     "4",
//     "stop",
// ]);

// sumPrimeNonPrime([
//     "30",
//     "83",
//     "33",
//     "-1",
//     "20",
//     "stop",
// ]);