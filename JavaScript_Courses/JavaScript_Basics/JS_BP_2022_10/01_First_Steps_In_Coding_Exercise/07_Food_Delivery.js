function foodDelivery(input) {
    let chickenPrice = 10.35;
    let fishPrice = 12.40;
    let vegPrice = 8.15;

    let delivery = 2.50;

    let chickenMenus = Number(input[0]);
    let fishMenus = Number(input[1]);
    let vegMenus = Number(input[2]);

    let totalPrice = chickenMenus * chickenPrice + fishMenus * fishPrice + vegMenus * vegPrice;

    let dessert = totalPrice * 0.20;

    let finalTotalPrice = totalPrice + dessert + delivery;

    console.log(finalTotalPrice);
}


// foodDelivery(["2", "4", "3"]);
