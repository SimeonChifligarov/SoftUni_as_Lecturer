function projectsCreation(input) {
    let architect = input[0];
    let projectsCount = Number(input[1]);  // 4
    let hoursNeeded = projectsCount * 3;

    let result = `The architect ${architect} will need ${hoursNeeded} hours to complete ${projectsCount} project/s.`
    console.log(result);
}


// projectsCreation(["George", "4"]);
