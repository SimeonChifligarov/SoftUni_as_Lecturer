function salary(input) {
    let penaltyFacebook = 150;
    let penaltyInstagram = 100;
    let penaltyReddit = 50;


    let openedTabs = Number(input[0]);
    let salary = Number(input[1]);

    // for (let i = 2; i < input.length; i++) {
    for (let i = 0; i < openedTabs; i++) {
        let website = input[i + 2];
        // console.log(website);
        if (website == "Facebook") {
            salary -= penaltyFacebook;
        } else if (website == "Instagram") {
            salary -= penaltyInstagram;
        } else if (website == "Reddit") {
            salary -= penaltyReddit;
        }
    }

    if (salary <= 0) {
        console.log("You have lost your salary.");
    } else {
        console.log(salary);
    }

}

// salary(["10", "750", "Facebook", "Dev.bg", "Instagram", "Facebook", "Reddit", "Facebook", "Facebook"]);
