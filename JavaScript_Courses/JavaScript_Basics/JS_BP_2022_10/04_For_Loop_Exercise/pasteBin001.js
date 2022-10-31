//   For Loop - Exercise
 
//   06. Oscars
 
function oscars(input){
 
    let actorName = input[0];
    let initialPoints = Number(input[1]);
    let judgeCount = Number(input[2])
    let i = input.length - (judgeCount*2); // Made for initial index selection// Works in judge when swapped with: let i = 3 
                                                   //Both ways work in VS Code!
    let currentJudge = input[3];
    let currentVote = Number(input[4]); 
    let judgePoints = initialPoints
    let hasPoints = false
    console.log(typeof(input.length));
    for(i = input.length - judgeCount*2; i < input.length;i++){
        currentJudge = input[i]
        currentVote = Number(input[++i])
        judgePoints += currentVote * currentJudge.length/2
        
        if(judgePoints > 1250.5){
            hasPoints = true
            break;
        }        
    }
    
    if(hasPoints){
        console.log(`Congratulations, ${actorName} got a nominee for leading role with ${judgePoints.toFixed(1)}!`);
 
    }else{
        console.log(`Sorry, ${actorName} you need ${(1250.5 - judgePoints).toFixed(1)} more!`);
    }
 
 
}
 
oscars(["Sandra Bullock","340","5","Robert De Niro","50","Julia Roberts","40.5","Daniel Day-Lewis","39.4","Nicolas Cage","29.9","Stoyanka Mutafova","33"])