function birthdayParty(input){
    let hallRent = Number(input[0]);
    let cake = 0;
    let drinks = 0;
    let animator = 0;
    let budget = 0;
 
    cake = hallRent * 0.20;
    drinks = cake - (cake * 0.45);
    animator = hallRent / 3;
 
    budget = hallRent + cake + drinks + animator;
    console.log(budget.toFixed(1));
}



birthdayParty([3720])