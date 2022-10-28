function basketballEquipment(input) {
    let annualFee = (input[0]);
 
    let sneakers = 0.60 * annualFee;
    let clothes = 0.80 * sneakers;
    let ball = 0.25 * clothes;
    let accessories = 0.20 * ball;
    let totalCosts = annualFee + sneakers + clothes + ball + accessories;
 
    console.log(totalCosts);
 
}
 
basketballEquipment(["365"]);
