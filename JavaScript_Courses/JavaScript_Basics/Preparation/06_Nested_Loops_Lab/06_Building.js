function building(input) {
    // две цели числа - броят на етажите и броят на стаите за един етаж. 
    let floors = Number(input[0]);
    let rooms = Number(input[1]);

    for (let i = floors; i > 0; i--) {
        let result = '';
        for (let j = 0; j < rooms; j++) {
            if (i == floors) {
                result += `L${i}${j} `;
            } else if (i % 2 == 0) {
                result += `O${i}${j} `;
            } else if (i % 2 == 1) {
                result += `A${i}${j} `;
            }
        }

        console.log(result);
    }
}


// building(["6", "4"]);
