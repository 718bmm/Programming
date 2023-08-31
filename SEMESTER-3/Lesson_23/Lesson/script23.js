const userData = new URLSearchParams(window.location.search);

// console.log(userData.get("name"));
// console.log(userData.get("about"));

// let first_name = document.querySelector("h1");
// let body = document.querySelector("p");

// first_name.innerHTML = userData.get("name");
// body.innerHTML = userData.get("about");


// console.log(userData.get("name"));
// console.log(userData.get("text"));
// console.log(userData.get("owner"));
// console.log(userData.get("time"));

let nname = document.querySelector("h1");
let text = document.querySelector("p");
let owner = document.querySelector("h1");
let time = document.querySelector("span");

nname.innerHTML = userData.get("nname");
text.innerHTML = userData.get("text");
owner.innerHTML = userData.get("owner");
time.innerHTML = userData.get("time");

// Страница для создания Статьи:
//     1. должна содержать форму (form) для создании статьи (название, текст статьи, кто создал, когда создал)
