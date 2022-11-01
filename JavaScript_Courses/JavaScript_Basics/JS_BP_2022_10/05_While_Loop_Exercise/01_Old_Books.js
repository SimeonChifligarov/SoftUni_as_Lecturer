function oldBooks(input) {
    let exitMessage = "No More Books";

    let booksChecked = 0;
    let targetBook = input[0];

    let index = 1;  // index; i;
    let currentBook = input[index];
    let isFound = false;


    while (currentBook != exitMessage) {
        booksChecked++;  // += 1;

        if (currentBook == targetBook) {
            // console.log(`You checked ${booksChecked - 1} books and found it.`);
            isFound = true;
            break;
        }


        index++;
        currentBook = input[index];
    }

    if (isFound === false) {
        console.log("The book you search is not here!");
        console.log(`You checked ${booksChecked} books.`);
    } else {
            console.log(`You checked ${booksChecked - 1} books and found it.`);
    }

}


// oldBooks([
//     "Troy",
//     "Stronger",
//     "Life Style",
//     "Troy",
// ]);

// oldBooks(["The Spot",
//     "Hunger Games",
//     "Harry Potter",
//     "Torronto",
//     "Spotify",
//     "No More Books"]);

// function oldBooks(input) {
//     let exitMessage = "No More Books";

//     let booksChecked = 0;
//     let targetBook = input[0];

//     let currentIndex = 1;  // index; i;
//     while (true) {
//         let currentBook = input[currentIndex];  // 1st iteration => "input[1]"
//         currentIndex++;  // 1st iteration => 2; 2nd iteration => 3;
//         booksChecked++;  // += 1;

//         if (currentBook == exitMessage) {  // true -> if library is done;
//             console.log("The book you search is not here!");
//             console.log(`You checked ${booksChecked - 1} books.`);
//             break;
//         }

//         if (currentBook == targetBook) {
//             console.log(`You checked ${booksChecked - 1} books and found it.`);
//             break;
//         }

//         // currentIndex++;
//     }

// // }