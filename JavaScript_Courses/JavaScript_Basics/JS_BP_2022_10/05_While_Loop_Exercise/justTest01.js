function oldBooks(input) {
    let bookCount=0;
 
    let i=0;
    let favBook=input[i];
    i++;
    let bookChek=input[i];
    while(bookChek !=favBook){
        bookChek=input[i];
        i++;
        if(bookChek==="No More Books"){
            console.log("The book you search is not here!")
            console.log(`You checked ${bookCount} books.`)
            break;
        }
        if (bookChek===favBook){
            console.log(`You checked ${bookCount} books and found it.`) ;
            break;           
        }
        bookCount++;
    }
    
    if (favBook == input[1]) {
        console.log(`You checked ${bookCount} books and found it.`) ;
    }
}


// oldBooks(["The Spot",
// "Hunger Games",
// "Harry Potter",
// "Torronto",
// "Spotify",
// "No More Books"]);

// oldBooks(['Troy', 'Troy'])