function usdToBgn(input) {
    let usdExchangeRate = 1.79549;

    let usd = Number(input[0]);
    let bgn = usd * usdExchangeRate;

    console.log(bgn);
}

// usdToBgn(["100"]);
