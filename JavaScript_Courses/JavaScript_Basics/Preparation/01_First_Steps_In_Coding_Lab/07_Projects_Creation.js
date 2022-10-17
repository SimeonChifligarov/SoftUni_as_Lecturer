function projectsCreation(nameAndProjects) {
    let name = nameAndProjects[0];
    let projectsNumbers = Number(nameAndProjects[1]);
    let hoursNeeded = projectsNumbers * 3;


    console.log(`The architect ${name} will need ${hoursNeeded} hours to complete ${projectsNumbers} project/s.`);
}

projectsCreation(["George ", "4"]);
