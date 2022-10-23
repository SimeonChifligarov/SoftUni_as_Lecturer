function trekkingMania(input) {
    let countMusala = 0;
    let countMonblan = 0;
    let countKilimangaro = 0;
    let countK2 = 0;
    let countEverest = 0;

    let countTotal = 0;

    let groups = Number(input[0]);

    for (let i = 0; i < groups; i++) {
        let currentGroup = Number(input[i + 1]);
        countTotal += currentGroup;

        if (currentGroup < 6) {
            countMusala += currentGroup;
        } else if (currentGroup < 13) {
            countMonblan += currentGroup;
        } else if (currentGroup < 26) {
            countKilimangaro += currentGroup;
        } else if (currentGroup < 41) {
            countK2 += currentGroup;
        } else if (currentGroup >= 41) {
            countEverest += currentGroup;
        }
    }

    console.log(`${((countMusala / countTotal) * 100).toFixed(2)}%`);
    console.log(`${((countMonblan / countTotal) * 100).toFixed(2)}%`);
    console.log(`${((countKilimangaro / countTotal) * 100).toFixed(2)}%`);
    console.log(`${((countK2 / countTotal) * 100).toFixed(2)}%`);
    console.log(`${((countEverest / countTotal) * 100).toFixed(2)}%`);

}


// trekkingMania(["10", "10", "5", "1", "100", "12", "26", "17", "37", "40", "78"]);
