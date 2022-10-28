function radiansToDegrees(input) {  // input = ["6.2832"] ; array с 1 елемент, к е на индекс 0 и е "6.2832"
    let radians = Number(input[0]);  // input[0] = "6.2832"; Number(input[0]) == Number("6.2832") == 6.2832
    let degrees = radians * 180 / Math.PI;

    console.log(degrees);
}

// radiansToDegrees(["6.2832"]);
