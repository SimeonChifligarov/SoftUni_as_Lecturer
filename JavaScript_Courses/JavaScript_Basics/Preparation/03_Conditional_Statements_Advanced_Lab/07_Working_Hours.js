function workingHours(input) {
    let hour = Number(input[0]);
    let day = input[1];

    if ((day == "Monday" || day == "Tuesday" || day == "Wednesday" || day == "Thursday"
        || day == "Friday" || day == "Saturday") && (hour >= 10 && hour <= 18)) {
            console.log("open");
        } else {
            console.log("closed");
        }
}

// workingHours(["11", "Monday"]);
