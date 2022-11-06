function hotelRoom(input) {
    let months = input[0];
    let numberOfNights = Number(input[1]);
    let studio = "";
    let apartment = "";
    let studioPrice = 0;
    let apartmentPrice = 0;
   
   
    if (months == "May" || months == "October") {
      studio = 50;
      apartment = 65;
      if (numberOfNights >= 7 && numberOfNights <= 14) {
        studioPrice = studio * numberOfNights * 0.95;
        apartmentPrice = apartment * numberOfNights;
      } else if (numberOfNights > 14) {
        studioPrice = studio * numberOfNights * 0.70;
        apartmentPrice = apartment * numberOfNights * 0.90;
      }
    } else if (months == "June" || months == "September") {
      studio = 75.20;
      apartment = 68.70;
      if (numberOfNights > 14) {
        studioPrice = studio * numberOfNights * 0.80;
        apartmentPrice = apartment * numberOfNights * 0.90;
      } else {
        studioPrice = studio * numberOfNights;
        apartmentPrice = apartment * numberOfNights;
      }
    } else if (months == "July" || months == "August") {
      studio = 76;
      apartment = 77;
      if (numberOfNights > 14) {
        studioPrice = studio * numberOfNights;
        apartmentPrice = apartment * numberOfNights * 0.90;
      } else{
        studioPrice = studio * numberOfNights;
        apartmentPrice = apartment * numberOfNights;
      }
    }
    console.log(`Apartment: ${(apartmentPrice).toFixed(2)} lv.`)
    console.log(`Studio: ${(studioPrice).toFixed(2)} lv.`)
  }
   
  // hotelRoom (["May","15"])
  // hotelRoom (["June","14"])
  // hotelRoom (["August","20"])
//   hotelRoom(["May","7"])