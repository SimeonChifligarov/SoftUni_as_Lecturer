function foodDelivery(input) {
    let chickenMenus = Number(input[0]);
    let fishMenus = Number(input[1]);
    let vegetarianMenus = Number(input[2]);

    let totalSum = chickenMenus * 10.35 + fishMenus * 12.40 + vegetarianMenus * 8.15;
    let totalSumWithDessert = totalSum * 1.20;
    let finalSum = totalSumWithDessert + 2.50;

    console.log(finalSum);
}

// foodDelivery(["2 ", "4 ", "3 "]);
// foodDelivery(["9 ", "2 ", "6 "]);
