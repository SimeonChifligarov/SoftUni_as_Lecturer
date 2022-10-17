function fishTank(input) {
    let length = Number(input[0]);
    let width = Number(input[1]);
    let heigth = Number(input[2]);

    let percentOff = Number(input[3]);

    let totalVolume = length * width * heigth / 1000;
    let activeVolume = totalVolume * (1 - percentOff / 100);

    console.log(activeVolume);
}


// fishTank(["85", "75", "47", "17"]);
// fishTank(["105", "77", "89", "18.5"]);
