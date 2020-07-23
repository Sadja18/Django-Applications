function hello(){
  console.log("Hello");
}

function helloUser(name="Guest User") {
  console.log("Hello "+name);
}

function addVar(var1, var2) {
  console.log(var1+var2);
}

function formal(title = "Sir ", name="Guest"){
  console.log(title+name);
  return name;
}

function table(num){
  for (var i = 1; i <=10; i++) {
    console.log(num + " * " + i + " = " + i*num);
  }
}

function geometricProgression(num, last_term = 12){

  for (var i = 1; i <=last_term ; i++) {
    console.log(num**i);
  }
}
