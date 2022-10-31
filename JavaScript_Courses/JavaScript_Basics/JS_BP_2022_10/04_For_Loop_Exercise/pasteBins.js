function equalPairs(input) {
    let n = Number(input[0]);
    let sum = 0;
    let temp = input[1] + input[2];
    let equal = "";
    let dif = 0;
    let min = input[1] + input[2];
    let max = input[1] + input[2];
    
      for (i = 1; i <= (2 * n); i += 2) {
        sum = input[i] + input[i + 1];
        if (sum > max) { max = sum;}
        else min = sum;
        if (temp == sum) {
            equal = "Yes";
        }
        else equal = "No";
        temp = sum;
    }
    dif = max - min;
    if (equal == "Yes") console.log(`Yes, value=${temp}`);
    else console.log(`No, maxdiff=${dif}`);
}
// equalPairs([3, 1, 2, 0, 3, 4, -1]);
// equalPairs([4, 1, 1, 3, 1, 2, 2, 0, 0]);
// equalPairs([2, -1, 0, 0, -1]);
// //equalPairs([2, 1, 2, 2, 2]);
// //equalPairs([3, -1, 2, 4, 4, 99, 100]);
// equalPairs([1, 5, 5]);
// equalPairs([2,-1,2,0,-1])
// equalPairs([8,5,5,70,-60,3,7,2,8,20,-10,15,-5,0,10,10,0]);
