function combinations(input) {
    //x1 + x2 + x3 =n
    let n = Number(input[0]);
    let validCombinationsCount = 0;
    let isFound = false;
    for (let x1 = 0; x1 <= n; x1++) {

        for (let x2 = 0; x2 <= n; x2++) {

            for (let x3 = 0; x3 <= n; x3++) {
                validCombinationsCount++;
                let result = x1 + x2 + x3;

                if (result == n) {
                    isFound = true;

                    break;
                }

            }
        }

        if (isFound == true) {
            break;
        }
    } console.log(`${validCombinationsCount}`);
}


// combinations (["25"])