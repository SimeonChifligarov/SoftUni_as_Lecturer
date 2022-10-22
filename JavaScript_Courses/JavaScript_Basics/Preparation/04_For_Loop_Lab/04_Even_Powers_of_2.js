function evenPowersOf2(input) {
    let number = Number(input[0]);

    for (let i = 0; i <= number; i += 2) {
        console.log(2 ** i);
    }
}

// evenPowersOf2(["6"]);
