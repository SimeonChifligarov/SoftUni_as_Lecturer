function petShop(input) {
    let dogsCount = Number(input[0]);
    let catsCount = Number(input[1]);

    let totalCost = dogsCount * 2.50 + catsCount * 4;

    let result = `${totalCost} lv.`

    console.log(result);
}


// petShop(["13", "9"]);
