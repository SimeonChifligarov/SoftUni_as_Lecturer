function concatenateData(input) {
    // име, фамилия, възраст и град 
    let firstName = input[0];
    let lastName = input[1];
    let age = Number(input[2]);
    let city = input[3];

    let result = `You are ${firstName} ${lastName}, a ${age}-years old person from ${city}.`;
    console.log(result);
}


// concatenateData(["Maria", "Ivanova", "20", "Sofia"]);
// concatenateData(["Gloria", "Georgieva", "25", "Plovdiv"]);
