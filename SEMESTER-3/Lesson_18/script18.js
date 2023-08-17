// function userInfo(name, psw = 'secret') {
    // console.log(`Your name is ${name} with psw: ${psw}`);
    // return `Your name is ${name} with psw: ${secret_psw}`;
    // Your name is BM with psw: *****
    // secret_psw = "";
    // for (let i = 0; i < psw.length; i++) {
    //     secret_psw += "*";
    // }
    // return `Your name is ${name} with psw: ${secret_psw}`
    // String repeat
// }

// result = userInfo("BM");
// console.log(userInfo("BM", "12345"))

// function multiply(a, b) {
//     a * b;
//     a * b;
//     return a * b;
// }

// (function (day) {
//     if (day === "Wednesday") {
//         return true;
//     }
//     return false;
// });

// const isWednesday = function (day) {
//     if (day === "Wednesday") {
//         return true;
//     }
//     return false;
// };

// console.log(isWednesday("Wednesday"));

// Arrow Functions
// const rectangleArea = (width, height) => {
//     let area = width * height;
//     return area;
// }

// console.log(rectangleArea(144, 455))
 
// const dummy = singleParam => singleParam + 2;
// console.log(dummy(2))
// const dummy = (singleParam) => {
//     if (singleParam) {
//         return true;
//     }
// };

// console.log(dummy(12))

// rock = 'RR'
// scissors = 'PP'
// paper = 'SS'

// function RPS(asa, sas) {
//     if (asa === scissors && sas === paper) {  
//         return `1:0 в пользу asa`
//     } else if (asa === rock && sas === scissors) {
//         return `1:0 в пользу asa`
//     } else if (asa === paper && sas === rock) {
//         return `1:0 в пользу asa`
//     } else if(sas === scissors && asa === paper) {  
//         return `1:0 в пользу sas`
//     } else if (sas === rock && asa === scissors) {
//         return `1:0 в пользу sas`
//     } else if (sas === paper && asa === rock) {
//         return `1:0 в пользу sas`
//     } else if(sas === paper && asa === paper) {  
//         return `ничья`
//     } else if (sas === rock && asa === rock) {
//         return `ничья`
//     } else if (sas === scissors && asa === scissors) {
//         return `ничья`
//     }
// }

// console.log(RPS(scissors, rock))

// Написать функцию для игры в камень-ножницы-бумага
// Rock, Paper, or Scissors
// The possible outcomes are:
// - Rock destroys scissors.
// - Scissors cut paper.
// - Paper covers rock.
// - If there’s a tie, then the game ends in a draw.

// var name = "BM"; // global
// let last_name = "Something";
// const age = 12;

// if (true) {
//     let last_name = "test_2"
//     const age = 32;
//     console.log(last_name, age);
// }

// console.log(last_name, age);

// function testScope() {
//     // локальный
//     var name; // undefined
//     name = "aaaaaaaaaaaa";
//     function testScope2() {
//         // локальный
//         var name;
//         name = 'AAAAAAAAHHHHH';
//     }
//     testScope2()
//     console.log(name)
// }

// testScope()
// console.log(name) 


