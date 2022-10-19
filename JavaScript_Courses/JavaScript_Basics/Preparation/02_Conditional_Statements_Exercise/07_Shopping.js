function shopping(input) {
    let videoCardPrice = 250;

    let budget = Number(input[0]);
    let videoCardsCount = Number(input[1]);
    let processorsCount = Number(input[2]);
    let ramCount = Number(input[3]);

    let videoCardsSum = videoCardsCount * videoCardPrice;
    let processorPrice = videoCardsSum * 0.35;
    let ramPrice = videoCardsSum * 0.10;

    let processorsSum = processorsCount * processorPrice;
    let ramSum = ramCount * ramPrice;

    let totalSum = videoCardsSum + processorsSum + ramSum;

    if (videoCardsCount > processorsCount) {
        totalSum *= 0.85;
    }

    if (budget >= totalSum) {
        console.log(`You have ${(budget - totalSum).toFixed(2)} leva left!`);
    } else {
        console.log(`Not enough money! You need ${(totalSum - budget).toFixed(2)} leva more!`);
    }
}

// shopping(["900", "2", "1", "3"]);
