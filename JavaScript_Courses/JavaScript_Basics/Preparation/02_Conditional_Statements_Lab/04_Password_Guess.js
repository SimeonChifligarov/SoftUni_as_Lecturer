function passwordGuess(input) {
    let realPassword = "s3cr3t!P@ssw0rd"
    let correctPassMsg = "Welcome"
    let wrongPassMsg = "Wrong password!"

    let triedPassword = input[0];

    if (triedPassword == realPassword) {
        console.log(correctPassMsg);
    } else {
        console.log(wrongPassMsg);
    }
}

// passwordGuess(["s3cr3t!P@ssw0rd"]);
// passwordGuess(["qwerty"]);
// passwordGuess(["s3cr3t!P@sswd"]);
