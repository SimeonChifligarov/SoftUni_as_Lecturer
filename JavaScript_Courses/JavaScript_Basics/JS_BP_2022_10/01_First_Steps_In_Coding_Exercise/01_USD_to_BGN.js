function usdToBgn(usdAsStringInArray) {
    let usdToBgnExchangeRate = 1.79;
    let usd = Number(usdAsStringInArray[0]); 
    let bgn = usd * usdToBgnExchangeRate;

    console.log(bgn);
}

// usdToBgn([22]);
// usdToBgn([100]);
