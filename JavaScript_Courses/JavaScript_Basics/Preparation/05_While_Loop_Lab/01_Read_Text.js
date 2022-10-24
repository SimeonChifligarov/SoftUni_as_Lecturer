function readText(input) {
    let i = 0;

    let currentWord = input[i];
    while (currentWord != "Stop") {
        console.log(currentWord);
        i++;
        currentWord = input[i];
    }
}


// readText(["Nakov",
//     "SoftUni",
//     "Sofia",
//     "Bulgaria",
//     "SomeText",
//     "Stop",
//     "AfterStop",
//     "Europe",
//     "HelloWorld"]);
