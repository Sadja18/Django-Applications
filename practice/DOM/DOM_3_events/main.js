var hd1 = document.querySelector("#hd1")

var hd2 = document.querySelector("#hd2")

var hd3 = document.querySelector("#hd3")
// console.log("Connected")

hd1.addEventListener("mouseover", function(){
  hd1.textContent = "Pointer Here";
  hd1.style.color = 'blue';
})

hd1.addEventListener("mouseout", function(){
  hd1.textContent = "Hover Here";
  hd1.style.color = 'black';
})

hd2.addEventListener("click",function(){
  hd2.textContent = "Clicked";
  hd2.style.color = "purple";
})

hd3.addEventListener("dblclick",function(){
  hd3.textContent = "Double Clicked";
  hd3.style.color = "red"
})

hd2.addEventListener("dblclick",function(){
  hd2.textContent = "Double Clicked";
  hd2.style.color = "red"
})
