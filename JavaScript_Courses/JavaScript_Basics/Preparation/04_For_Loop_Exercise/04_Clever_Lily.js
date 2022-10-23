function cleverLily(input) {
    let age = Number(input[0]);
    let washingMachinePrice = Number(input[1]);
    let toyPrice = Number(input[2]);

    let toyCount = 0;

    let totalMoney = 0;
    let giftMoney = 10;

    for (let i = 1; i <= age; i++) {
        if (i % 2 == 1) {
            toyCount++; // toyCount += 1;
        } else {
            // totalMoney += i * 5;
            totalMoney += giftMoney;
            totalMoney--;
            giftMoney += 10;
        }
    }

    totalMoney += toyCount * toyPrice;

    if (totalMoney >= washingMachinePrice) {
        console.log(`Yes! ${(totalMoney - washingMachinePrice).toFixed(2)}`);
    } else {
        console.log(`No! ${(washingMachinePrice - totalMoney).toFixed(2)}`);
    }
}

// cleverLily(["10", "170.00", "6"]);
