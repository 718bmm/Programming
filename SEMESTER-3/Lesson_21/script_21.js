// document.title.innerHTML = "Cats";
// document.body.innerHTML = "<h1>Some love to cats!</h1>";

let paragraph = document.querySelector("p");
let paragraphs = document.querySelectorAll("p");
paragraph.innerHTML = "Bah";
paragraphs[2].innerHTML = "poter";

document.getElementById("bio").innerHTML = "Everyone is sleepy";
document.getElementsByClassName("test")[0].innerHTML = "Not a Test";
// document.getElementsByTagName("ul")[0].innerHTML = "EEEEEEEEEEEEEEEEEEEE";

let list = document.querySelector("ul");
// list.style.listStyleType = "none";

// list.style.backgroundColor = `rgb(${100}, ${200}, ${100})`;
// list.style.color = `#fff`;
// list.classList = "container";

// children - вохвращает список детей выделенного тэга
// parentElement - возвращает родителя выделенного тэга


// console.log(paragraphs);

// document.querySelectorAll()

// let p = document.querySelector(".blue");
// p.innerHTML = "Some text";
// p.style.color = "blue";
// p.style.fontSize = "2em";

// let liTagParent = document.querySelector("li.blue").parentElement;
// console.log(liTagParent.parentElement);
// liTagParent.children[0].innerHTML = "Yeah";
// liTagParent.style.backgroundColor = "biege";

// liTagParent.classList = "green";
// console.log(liTagParent);

// let eventTarget = document.getElementById("targetElement");

// eventTarget.addEventListener("click", function () {
//   liTagParent.style.backgroundColor = "biege";
//   // this block of code will run when click event happens on eventTarget element
// });

// const array1 = [1, 2, 3, 4];

// // 0 + 1 + 2 + 3 + 4
// const initialValue = 0;
// const sumWithInitial = array1.reduce((accumulator, currentValue) => {
//   console.log("accumulator", accumulator, "currentValue", currentValue);
//   return accumulator - currentValue; // 1
// }, "");
// "" + 1 = "1"
// "1" + 1 = "1"

// console.log(sumWithInitial);
