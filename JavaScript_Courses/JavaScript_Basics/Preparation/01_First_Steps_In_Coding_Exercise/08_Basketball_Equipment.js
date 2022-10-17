function basketballEquipment(input) {
    let yearFee = Number(input[0]);

    let shoes = 0.60 * yearFee;
    let equip = 0.80 * shoes;
    let ball = 0.25 * equip;
    let accessoirs = 0.20 * ball;

    let total = yearFee + shoes + equip + ball + accessoirs;

    console.log(total);
}

// basketballEquipment(["365"]);
// basketballEquipment(["550"]);
