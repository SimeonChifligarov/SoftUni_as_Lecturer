function cinemaTickets(input) { 
    let studentCurrent = 0;
    let stardardCurrent = 0;
    let kidCurrent = 0;
    
    let totalTickets = 0;
    
    
    let i = 0;
    let currentMovie = input[i];
    i++;
    
    while (currentMovie != 'Finish') {
    let seatAvailable = Number(input[i]);
    i++;
    let seatBougth = 0;
    
    while (true) {
    if (seatAvailable == seatBougth) {
    break;
    }
    
    let currentTicket = input[i];  
    i++;
    
    if (currentTicket == "End") {
    break;
    }
    
    seatBougth++;
    totalTickets++;
    if (currentTicket == "student") {
    studentCurrent++;
    } else if (currentTicket == "standard") {
    stardardCurrent++;
    } else if (currentTicket == "kid") {
    kidCurrent++;
    }
    
    }
    
    
    console.log(`${currentMovie} - ${(100 * seatBougth / seatAvailable).toFixed(2)}% full.`);
    
    
    currentMovie = input[i];
    i++;
    }
    
    
    console.log(`Total tickets: ${totalTickets}`);  
    console.log(`${(100 * studentCurrent / totalTickets).toFixed(2)}% student tickets.`);
    console.log(`${(100 * stardardCurrent / totalTickets).toFixed(2)}% standard tickets.`);
    console.log(`${(100 * kidCurrent / totalTickets).toFixed(2)}% kids tickets.`);
    
    }


// cinemaTickets([
//     "Taxi",
//     "10",
//     "standard",
//     "kid",
//     "student",
//     "student",
//     "standard",
//     "standard",
//     "End",
//     "Scary Movie",
//     "6",
//     "student",
//     "student",
//     "student",
//     "student",
//     "student",
//     "student",
//     "Finish",
// ]);
