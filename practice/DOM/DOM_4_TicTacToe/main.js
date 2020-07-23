// console.log("Connected")

// Restart
var restart = document.querySelector("#button1");

// Grab all squares
var square = document.querySelectorAll("td");

// Clear squares
function clearBoard(){
  for (var i = 0; i < square.length; i++) {
    square[i].textContent = "";
  }
}

restart.addEventListener("click", clearBoard);

// Check square marker
/*
var cell11 = document.querySelector("#td11");
var cell12 = document.querySelector("#td12");
var cell13 = document.querySelector("#td13");
var cell21 = document.querySelector("#td21");
var cell22 = document.querySelector("#td22");
var cell23 = document.querySelector("#td23");
var cell31 = document.querySelector("#td31");
var cell32 = document.querySelector("#td32");
var cell33 = document.querySelector("#td33");
*/

function changemark(){
  if (this.textContent === "") {
    this.textContent = "X";
  }else if (this.textContent==="X") {
    this.textContent = "O";
  }else {
    this.textContent = "";
  }
}

// add event listeners to all squares
/*
cell11.addEventListener("click", function(){
  if (cell11.textContent === "") {
    cell11.textContent = "X";
  }else if (cell11.textContent==="X") {
    cell11.textContent = "O";
  }else {
    cell11.textContent = "";
  }
})

cell12.addEventListener("click", function(){
  if (cell12.textContent === "") {
    cell12.textContent = "X";
  }else if (cell12.textContent==="X") {
    cell12.textContent = "O";
  }else {
    cell12.textContent = "";
  }
})

cell13.addEventListener("click", function(){
  if (cell13.textContent === "") {
    cell13.textContent = "X";
  }else if (cell13.textContent==="X") {
    cell13.textContent = "O";
  }else {
    cell13.textContent = "";
  }
})

cell21.addEventListener("click", function(){
  if (cell21.textContent === "") {
    cell21.textContent = "X";
  }else if (cell21.textContent==="X") {
    cell21.textContent = "O";
  }else {
    cell21.textContent = "";
  }
})

cell22.addEventListener("click", function(){
  if (cell22.textContent === "") {
    cell22.textContent = "X";
  }else if (cell22.textContent==="X") {
    cell22.textContent = "O";
  }else {
    cell22.textContent = "";
  }
})

cell23.addEventListener("click", function(){
  if (cell23.textContent === "") {
    cell23.textContent = "X";
  }else if (cell23.textContent==="X") {
    cell23.textContent = "O";
  }else {
    cell23.textContent = "";
  }
})

cell31.addEventListener("click", function(){
  if (cell31.textContent === "") {
    cell31.textContent = "X";
  }else if (cell31.textContent==="X") {
    cell31.textContent = "O";
  }else {
    cell31.textContent = "";
  }
})

cell32.addEventListener("click", function(){
  if (cell32.textContent === "") {
    cell32.textContent = "X";
  }else if (cell32.textContent==="X") {
    cell32.textContent = "O";
  }else {
    cell32.textContent = "";
  }
})

cell33.addEventListener("click", function(){
  if (cell33.textContent === "") {
    cell33.textContent = "X";
  }else if (cell33.textContent==="X") {
    cell33.textContent = "O";
  }else {
    cell33.textContent = "";
  }
})
*/
for (var i = 0; i < square.length; i++) {
  square[i].addEventListener("click", changemark);
}
