// console.log(first);

// var first = 1;
// let second;

// console.log(first);

// const third = 'third value';

// first = true;

// let w = 4;
// w = w + 1;
// w += 1;
// w++; // +1
// console.log(w);
// w--; // +1
// console.log(w);
// // -= /= *=

// const myPet = 'armadillo';
// console.log(`I own a pet ${myPet}.`);
// console.log("I own a pet " + myPet);

// console.log(typeof 1);
// console.log(typeof "You");
// console.log(typeof true);

// console.log("dsad asdsa d23f3".split(" "))
// console.log("dsad asdsa d23f3".slice(" "))
// console.log("dsad asdsa d23f3".charAt("3"))

// if ("") {
//     console.log("It works");
// } else {
//     console.log("It doesn't works");
// }

// let age = 12;
// let name = 'Yohan';

// and 
// if (age >= 18 && name === "Yohan") {
//     console.log(`First: Your data: age: ${age}, name: ${name}`)
// }   else if (age == 12 && name === "Yohan") {
//     console.log(`Second: Your data: age: ${age}, name: ${name}`)
// }   else {
//     console.log("No matches.")
// }

// or 
// if (age >= 18 || name === "Yohan") {
//     console.log(`First: Your data: age: ${age}, name: ${name}`)
// }   else if (age == 12 || name === "Yohan") {
//     console.log(`Second: Your data: age: ${age}, name: ${name}`)
// }   else {
//     console.log("No matches.")
// }

// if (!true) {
//     console.log(true);
// }   else {
//     console.log(false)
// }

// if (!(1 === 1)) {
//     console.log(true);
// }   else {
//     console.log(false)
// }


// let age = 18;

// if (age >= 18) {
//     console.log('Turn on the lights!');
// }   else {
//     console.log('Turn off the lights!');
// }

// // ternary
// age >= 18 ? console.log('Turn on the lights!') : console.log('Turn off the lights!');
// for (let counter = 0; counter < 4; counter++) {
//     console.log(counter);
// }

// let name = "Behruz";
// for (let i = 0; i < name.length; i++) {
//     console.log(name[i]); 
// }

// Function
let age = 18;
function checkAge (age, name='Behruz') {
    console.log(`Your age is ${age} and name ${name}`)
}

// checkAge();
// checkAge(age);
checkAge(age, "John");
checkAge(age, name="Yohan");


function checkAge (age, name='Behruz') {
    if (age >= 18 || name === "Yohan") {
        console.log(`First: Your data: age: ${age}, name: ${name}`)
    }   else if (age == 12 || name === "Yohan") {
        console.log(`Second: Your data: age: ${age}, name: ${name}`)
    }   else {
        console.log("No matches.")
    }
    return "smth went wrong"
}

console.log(checkAge(12))

// if (age > 18) {
//     console.log(`It works! Your age ${age}`);
// }   else if (age === 12) { // ==
//     console.log(`Your age ${age}`);
// }   else if (age === 13) { // ==
//     console.log(`Your age ${age}`);
// }   else if (age === 14) { // ==
//     console.log(`Your age ${age}`);
// }   else if (age === 15) { // ==
//     console.log(`Your age ${age}`);
// }   else {
//     console.log("It doesn't works");
// }


// let groceryItem = 'papaya';

// switch (groceryItem) {
//     case 'tomato':
//         console.log("Tomatoes are $0.49");
//         break;
//     case 'papaya':
//         console.log("Papayas are $1.29");
//         break;
//     case 'lime':
//         console.log("Limes are $1.49");
//         break;
//     default:
//         console.log("Invalid item");
//         break;
// }








