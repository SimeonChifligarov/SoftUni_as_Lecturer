function cinemaTickets(input) {
    let studentCount = 0;
    let standardCount = 0;
    let kidCount = 0;

    let i = 0;

    while (true) {
        let movie = input[i];

        if (movie == "Finish") {
            break;
        }

        i++;
        let seatsAvailable = Number(input[i]);
        let seatsBought = 0;

        while (seatsAvailable > seatsBought) {
            i++;
            let currentSeat = input[i];

            if (currentSeat == "End") {
                break;
            }

            seatsBought++;
            if (currentSeat == "student") {
                studentCount++;
            } else if (currentSeat == "standard") {
                standardCount++;
            } else if (currentSeat == "kid") {
                kidCount++;
            }
        }

        console.log(`${movie} - ${((seatsBought / seatsAvailable) * 100).toFixed(2)}% full.`);
        i++;
    }

    let totalTickets = studentCount + standardCount + kidCount;
    console.log(`Total tickets: ${totalTickets}}`);
    console.log(`${(studentCount / totalTickets * 100).toFixed(2)}% student tickets.`);
    console.log(`${(standardCount / totalTickets * 100).toFixed(2)}% student tickets.`);
    console.log(`${(kidCount / totalTickets * 100).toFixed(2)}% student tickets.`);
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
