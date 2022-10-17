function petShop(input) {
    let dogFoods = Number(input[0]);
    let catFoods = input[1];

    let total = dogFoods * 2.5 + catFoods * 4;

    console.log(`${total} lv.`);
}

petShop(["5 ", "4 "]);
