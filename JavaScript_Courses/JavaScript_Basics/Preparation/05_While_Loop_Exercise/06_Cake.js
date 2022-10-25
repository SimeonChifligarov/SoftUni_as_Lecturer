function cake(input) {
    let width = Number(input[0]);
    let length = Number(input[1]);
    let cakePieces = width * length;

    let currentIndex = 2;

    while (true) {
        let currentPiece = input[currentIndex];

        if (currentPiece == "STOP") {
            console.log(`${cakePieces} pieces are left.`);
            break;
        }

        cakePieces -= Number(currentPiece);
        if (cakePieces < 0) {
            console.log(`No more cake left! You need ${-cakePieces} pieces more.`);
            break;
        }

        currentIndex++;
    }
}


// function cake(input) {
//     let width = Number(input[0]);
//     let length = Number(input[1]);
//     let cakePieces = width * length;

//     let currentIndex = 2;
//     let currentPiece = input[currentIndex];
//     while (currentPiece != "STOP") {
//         cakePieces -= Number(currentPiece);
//         if (cakePieces < 0) {
//             console.log(`No more cake left! You need ${-cakePieces} pieces more.`);
//             break;
//         }

//         currentIndex++;
//         currentPiece = input[currentIndex];
//     }

//     if (currentPiece == "STOP") {
//         console.log(`${cakePieces} pieces are left.`);
//     }
// }


// cake([
//     "10",
//     "10",
//     "20",
//     "20",
//     "20",
//     "20",
//     "21"
// ]);
