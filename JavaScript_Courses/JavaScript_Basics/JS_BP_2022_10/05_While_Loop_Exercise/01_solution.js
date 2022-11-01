function oldBooks(input)
{
 
    let index = 0;
    let favoriteBook = input[index];
    index++;
    let library = input[index];
    index++;
    let count = 0;
    //console.log(biblioteca);
 
    while(library !== favoriteBook)
    {
        //console.log(library); 
 
       if(library === 'No More Books')
       {
        console.log(`The book you search is not here!`);
        console.log(`You checked ${count} books.`);
		break;
       }
       library = input[index];
       index++;
       count++;
 
    }

    if (library == favoriteBook) {
        console.log(`You checked ${count} books and found it.`);
    }
}
 
// oldBooks(["Troy",
// "Stronger",
// "Life Style",
// "Troy"]);
 
// oldBooks(["The Spot",
// "Hunger Games",
// "Harry Potter",
// "Torronto",
// "Spotify",
// "No More Books"]);
 
// oldBooks(["Bourne",
// "True Story",
// "Forever",
// "More Space",
// "The Girl",
// "Spaceship",
// "Strongest",
// "Profit",
// "Tripple",
// "Stella",
// "The Matrix",
// "Bourne"]);