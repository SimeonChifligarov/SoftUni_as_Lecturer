function oldBooks(input) {
    let targetBook = input[0];
    let currentIndex = 1;
    let checkedBook = 0;

    while (true) {
        let currentBook = input[currentIndex];

        if (currentBook == "No More Books") {
            console.log("The book you search is not here!");
            console.log(`You checked ${checkedBook} books.`);
            break;
        }

        checkedBook++;
        if (currentBook == targetBook) {
            console.log(`You checked ${checkedBook - 1} books and found it.`);
            break;
        }

        currentIndex++;
    }
}


// oldBooks([
//     "Troy",
//     "Stronger",
//     "Life Style",
//     "Troy"
// ]);
