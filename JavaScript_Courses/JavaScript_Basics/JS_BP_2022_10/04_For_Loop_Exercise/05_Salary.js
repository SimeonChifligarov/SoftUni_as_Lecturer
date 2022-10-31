function salary(input) {
    let penaltyFacebook = 150;
    let penaltyInstagram = 100;
    let penaltyReddit = 50;

    let openedTabs = Number(input[0]);  // 10;
    let salary = Number(input[1]);

    // console.log(input.length);
    // for (let i = 0; i < openedTabs; i++) {
    for (let i = 0; i < input.length - 2; i++) {
        let websiteName = input[i + 2];  // 1. iter => input[0 + 2] == input[2];
        // console.log(websiteName);
        if (websiteName == 'Facebook') {
            salary -= penaltyFacebook;
        } else if (websiteName == 'Instagram') {
            salary -= penaltyInstagram;
        } else if (websiteName == 'Reddit') {
            salary -= penaltyReddit;
        }
    }

    if (salary <= 0) {
        console.log('You have lost your salary.');
    } else {
        console.log(salary);
    }
}


// salary([
//     "10",
//     "750",
//     "Facebook",
//     "Dev.bg",
//     "Instagram",
//     "Facebook",
//     "Reddit",
//     "Facebook",
//     "Facebook",
// ]);

// salary([
//     "3",
//     "500",
//     "Github.com",
//     "Stackoverflow.com",
//     "softuni.bg",
// ]);
