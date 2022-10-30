function skiTrip(input) {
    let roomForOne = 18;
    let apartment = 25;
    let presidentApartment = 35;
    
    let days = Number(input[0]);
    let nigths = days - 1;
    let roomType = input[1];
    let happy = input[2];  // "positive"  или "negative"
    
    let roomPrice = 0;

    if (roomType == "room for one person") {
        roomPrice = roomForOne;
    } else if (roomType == "apartment") {
        roomPrice = apartment;
    } else if (roomType == "president apartment") {
        roomPrice = presidentApartment;
    }

    let totalCost = roomPrice * nigths;
    if (roomType == "apartment") {
        if (nigths < 10) {
            totalCost *= 0.70;
        } else if (nigths <= 15) {
            totalCost *= 0.65;
        } else if (nigths > 15) {
            totalCost *= 0.50;
        }

    } else if (roomType == "president apartment") {
        if (nigths < 10) {
            totalCost *= 0.90;
        } else if (nigths <= 15) {
            totalCost *= 0.85;
        } else if (nigths > 15) {
            totalCost *= 0.80;
        }
    }

    if (happy == "positive") {
        totalCost *= 1.25;
    } else if (happy == "negative") {
        totalCost *= 0.90;
    }

    console.log(totalCost.toFixed(2));
}


// skiTrip(["14", "apartment", "positive"]);
