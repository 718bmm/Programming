// const bankAccount = {
//     _amount: 1000,
// }
// // even though it's not recommended we can still change this property
// bankAccount._amount = 1000000;
// console.log(bankAccount);

const robot = {
    _energyLevel: 100,
    recharge() {
        this._energyLevel += 30;
        console.log(`Recharged! Energy is currently at ${this._energyLevel}%.`);
    },
};

// robot._energyLevel = 'High';
// robot.recharge();
// console.log(robot._energyLevel);

const person = {
    _firstName: "John",
    _lastName: "Doe",
    _age: 37,
    // fullName: "Francisco Buele", // не делать
    get fullName() {
        if (this._firstName && this._lastName) {
            return `${this._firstName} ${this._lastName}`;
        } else {
            return "Missing a first name or last name.";
        }
    },
    set age(newAge) {
        if (typeof newAge === "number") {
            this._age = newAge;
        } else {
            console.log("You must assign a number to age");
        }
    },
    get age() {
        if (this._age) {
            return this._age;
        } else {
            return "Age id empty or is 0."
        }
    }
}

// person.age = "40";
// console.log(person.fullName);
// console.log(person.age);



const menu = {
    _meal: "Steak",
    _price: 110,
    
    get getter_m() {
        if (this._meal) {
            return this._meal;
        } else {
            return "Error";
        }
    },
    get getter_p() {
        if (this.price) {
            return this._price;
        } else {
            return "Error";
        }
    },
    set setter_m(meal) {
        if (this._meal === "string") {
            this._meal = meal;
        } else {
            return "Error";
        }
    },
    set setter_p(price) {
        if (this._price === "number") {
            this.price = price;
        } else {
            return "Error";
        }
    },
}

console.log(menu);





// Создать объект menu, который составляет дневное меню для кафе
// оно состоит из двух приватных атрибутов meal и price
// Создать для них getter и setter, чтобы изменять и получать эти объекта
