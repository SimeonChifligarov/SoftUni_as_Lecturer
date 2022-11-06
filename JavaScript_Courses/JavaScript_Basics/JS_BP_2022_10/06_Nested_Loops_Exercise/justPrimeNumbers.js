// 7 % 2 != 0                      2048 % 2 != 0
// 7 % 3 != 0
// 7 % 4 != 0
// 7 % 5 != 0
// 7 % 6 != 0
//    [7 - 1]

let a = 17;

let isPrime = true;
for (let j = 2; j <= (a - 1); j++) {
    if (a % j == 0) {
        isPrime = false;
        break;
    }
}

console.log(isPrime);

