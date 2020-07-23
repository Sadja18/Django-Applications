var fname = prompt("Enter FIRST NAME: ")
var lname = prompt("Enter LAST NAME: ")

var age = prompt("Enter Age: ")
var height = prompt("Enter Height: ")

var petname = prompt("Enter Pet Name: ")
alert("Thanks you for the information");

var name_check = null;
var age_check = null;
var ht_check = null;
var pname_check = null;

if (fname[0] === lname[0]){
  name_check = true;
}else {
  name_check = false;
}
if (age>20 && age<30){
  age_check = true;
}else {
  age_check = false;
}
if (height>=170) {
  ht_check = true;
}else {
  ht_check = false;
}
if (petname[petname.length-1] === "y" || petname[petname.length-1] === "Y"){;
  pname_check = true;
}else {
  pname_check = false;
}
// console.log(name_check+" "+age_check+ " "+ht_check+" "+pname_check);
if (name_check && age_check && ht_check && pname_check){
  console.log("You passed");
}else {
  console.log("Didn't pass");
}
