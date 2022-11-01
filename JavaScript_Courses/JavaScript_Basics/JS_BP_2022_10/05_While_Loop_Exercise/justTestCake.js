function cake(input) {
    let width = Number(input[0])
    let length = Number(input[1])
    let totalCake = width * length
    let cakeLeft = totalCake
    let i = 2
 
    while (true) {
        let currentCommand = input[i]
        i++
        if (currentCommand == "STOP") {
            console.log(`${cakeLeft} pieces are left.`);
            break
        }
        let currentPieces = Number(currentCommand)
        cakeLeft -= currentPieces
        if (cakeLeft < 0) {
            console.log(`No more cake left! You need ${-cakeLeft} pieces more.`);
            break
        }
    }
}



// cake(["10",
// "2",
// "2",
// "4",
// "6",
// "STOP"])