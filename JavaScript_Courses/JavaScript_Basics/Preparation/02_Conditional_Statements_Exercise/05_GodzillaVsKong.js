function godzillaVsKong(input) {
    let budget = Number(input[0]);
    let statists = Number(input[1]);
    let clothesPrice = Number(input[2]);

    let decor = budget * 0.10;
    let clothesAll = statists * clothesPrice;

    if (statists > 150) {
        clothesAll *= 0.90;
    }

    let expenses = decor + clothesAll;

    if (expenses > budget) {
        console.log('Not enough money!');
        console.log(`Wingard needs ${(expenses - budget).toFixed(2)} leva more.`);
    } else {
        console.log('Action!');
        console.log(`Wingard starts filming with ${(budget - expenses).toFixed(2)} leva left.`);
    }
}


// godzillaVsKong(["15437.62", "186", "57.99"]);
