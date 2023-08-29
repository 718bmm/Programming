// parentNode
// children

// let anchor = document.getElementsByTagName
// let anchor = document.querySelector("a");
// console.log(anchor.parentNode);
// anchor.parentNode.style.fontSize = "20px";
// console.log(anchor.children);
// anchor.children[0].style.display = "block";

// let paragraph = document.createElement("p");
// paragraph.id = "info";
// paragraph.innerHTML = "THe text inside the paragraph";

// document.body.append(paragraph);

// let paragraph_2 = document.querySelector("body>p");
// // let paragraph_2 = document.querySelector("div>p");
// console.log(paragraph_2);
// document.querySelector("div").removeChild(paragraph_2);

// // Удаляет только если это прямой ребёнок
// document.body.removeChild(paragraph_2);

// // to hide elemenet we can use hidden property
// document.getElementById("sign").hidden = "true"

let changeColor = document.querySelector("img");

// changeColor.onclick = function () {
//     let red = Math.random() * 255;
//     let green = Math.random() * 255;
//     let blue = Math.random() * 255; 
//     document.body.style.backgroundColor = `rgb(${red}, ${green}, ${blue})`;
// };

function bgColorGenerator() {
    let red = Math.random() * 255;
    let green = Math.random() * 255;
    let blue = Math.random() * 255; 
    document.body.style.backgroundColor = `rgb(${red}, ${green}, ${blue})`;
}

// changeColor.onclick= bgColorGenerator;

changeColor.addEventListener("click", bgColorGenerator);

let fortunes = [
    "A beautiful, smart, and loving person will be coming into your life.", 
    "A fresh start will put you on your way.",
    "A golden egg of opportunity falls into your lap this month.",
    "A smile is your personal welcome mat.",
    "All your hard work will soon pay off.",
];

let button = document.getElementById("fortuneButton");
let fortune = document.getElementById("fortune");

function fortuneSelector() {
    let randomFortune = Math.floor(Math.random() * fortunes.length);
    return fortunes [randomFortune];
}

const change = [
    {
        bgColor: "red",
        fontSize: "10px",
        fontFamily: "Calibri",
    }
]

let a; 
function showFortune(event) {
    a = event;
    fortune.innerHTML = fortuneSelector();
    button.innerHTML = "Come back tomorrow!";
    button.style.cursor = "default";

    //add your code here
    button.removeEventListener("click", showFortune);
}

button.addEventListener("click", showFortune);


// Создать и Поставить тэг с текстом "Change ME!" в центр и сделать так. чтобы при нажатии менялся background-color body, font-size и font-family тэга с текстом



function changeStyles() {
    var body = document.getElementsByTagName("body")[0];
    var h1 = document.getElementById("changeColor");

    var randomColor = '#' + Math.floor(Math.random()*16777215).toString(16);
    var randomFontSize = Math.floor(Math.random() * 30) + 10;
    var fonts = ['Arial', 'Helvetica', 'Verdana', 'Georgia', 'Times New Roman'];
    var randomFontFamily = fonts[Math.floor(Math.random() * fonts.length)];

    // Assign new styles to elements
    body.style.backgroundColor = randomColor;
    h1.style.fontSize = randomFontSize + "px";
    h1.style.fontFamily = randomFontFamily;
}