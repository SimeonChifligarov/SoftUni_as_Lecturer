function suppliesForSchool(input) {
    let pensNums = Number(input[0]);
    let markersNums = Number(input[1]);
    let someLiters = Number(input[2]);
    let discountPercent = Number(input[3]);

    let totalSum = pensNums * 5.80 + markersNums * 7.20 + someLiters * 1.20;
    let totalSumAfterDiscount = totalSum * (1 - discountPercent / 100);

    console.log(totalSumAfterDiscount);
}

// suppliesForSchool(["2", "3", "4", "25"]);
// suppliesForSchool(["4 ", "2 ", "5 ", "13 "]);
