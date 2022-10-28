function basketballEquipment(input) {
    let annualFee = Number(input[0]);

    let shoes = annualFee * (100 - 40) / 100;
    let equip = shoes * (1 - 0.2);
    let ball = equip / 4;
    let accessoirs = ball / 5;

    let totalCosts = annualFee + shoes + equip + ball + accessoirs;

    console.log(totalCosts);
}

// basketballEquipment(["550 "]);
