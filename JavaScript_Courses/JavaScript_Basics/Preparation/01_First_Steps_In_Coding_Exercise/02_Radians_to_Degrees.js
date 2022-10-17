function radiansToDegrees(input) {
    let radiansAsString = input[0];
    let radians = Number(radiansAsString);

    let degrees = radians * 180 / Math.PI;

    console.log(degrees);
}

// radiansToDegrees(["3.1416"]);
