function sumPrimeNonPrime(input) {  // ["3","9","0","7","19","4","stop"]
    let sumPrimes = 0;
    let sumNonPrimes = 0;

    let i = 0;
    let currentCommand = input[i];
    i++;

    while (currentCommand != 'stop') {
        let currentNumber = Number(currentCommand);

        if (currentNumber < 0) {
            console.log('Number is negative.');
            currentCommand = input[i];
            i++;
            continue;
        }


        let isPrime = true;
        for (let j = 2; j <= (currentNumber - 1); j++) {
            if (currentNumber % j == 0) {
                isPrime = false;
                break;
            }
        }

        if (isPrime == true) {
            sumPrimes += currentNumber;
        } else {
            sumNonPrimes += currentNumber;
        }
        
        currentCommand = input[i];
        i++;
    }

    console.log(`Sum of all prime numbers is: ${sumPrimes}`);
    console.log(`Sum of all non prime numbers is: ${sumNonPrimes}`);

}


// sumPrimeNonPrime(["3",
//     "9",
//     "0",
//     "7",
//     "19",
//     "4",
//     "stop"]);

// sumPrimeNonPrime(["30",
//     "83",
//     "33",
//     "-1",
//     "20",
//     "stop"]);