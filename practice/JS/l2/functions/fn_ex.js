//Problem 1
function sleepIn(weekday, vacation) {
    //Code Goes Here
  return (!weekday || vacation);
}

//Problem 2

function monkeyTrouble(aSmile, bSmile) {
    //Code Goes Here
    return (aSmile && bSmile) || (!aSmile && !bSmile);
}

// PROBLEM 3: STRING TIMES
function stringTimes(str, n) {
    //Code Goes Here
    var returnStr = '';
    var i = 0;
    while (i < n) {
        returnStr += str;
        i++;
    }
    return returnStr;
}

// PROBLEM 4: LUCKY SUM
function luckySum(a, b, c){

  //Code Goes Here
  if(a == 13){
    return 0
  }
  if(b == 13){
    return a
  }
  if(c == 13){
    return a + b
  }
  return a + b + c
}

// PROBLEM 5:

function caught_speeding(speed, is_birthday){
  //Code Goes Here
  if(is_birthday){
    speed -= 5
  }
  if(speed <= 60){
      return 0
  }
  // Optional: (60 < speed && speed <=80)
  if(60 < speed <= 80){
    return 1
  }
  return 2
}

// BONUS: MAKE BRICKS

function makeBricks(small, big, goal){
  //Code Goes Here
  return goal%5 >= 0 && goal%5 - small <= 0 && small + 5*big >= goal
}
