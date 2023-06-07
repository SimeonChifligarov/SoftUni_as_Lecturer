function yardGreening(input) {
    let squaredMeters = Number(input[0]);

    let totalCost = squaredMeters * 7.61;
    let discount = totalCost * 0.18;  // 18 / 100;

    console.log(`The final price is: ${totalCost - discount} lv.`);
    console.log(`The discount is: ${discount} lv.`);
}


// yardGreening(["550"]);
