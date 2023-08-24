let menu = {
    _meal: "Meal",
    _price: 10,

    get getter_m() {
        if (this._meal && typeof this._meal === "string") {
            return this._meal;
        } else {
            return "Error"
        }
    },

    get getter_p() {
        if (typeof this._price === "number" && this._price) {
            return this._price;
        } else {
            return "Error"
        }
    },

    set setter_m(newValue) {
        if (typeof newValue === "string" && newValue) {
            this._meal = newValue;
        } else {
            console.log("Error");
        }
    },
        
    set setter_p(newPrice) {
        if (typeof this._price === "number" && newPrice) {
            this._price = newPrice;
        } else {
            console.log("Error");
        }
    }
  };
  
  menu.getter_m = "Another meal";
  console.log(menu.getter_m);
  menu.getter_p = 20.45;
  console.log(menu.getter_p);



// 1. forEach: Выполняет указанную функцию один раз для каждого элемента массива.
const a = [1, 2, 3, 4, 5];
a.forEach(function(item) {
  console.log(item);
});


// 2. map: Создает новый массив, в котором каждый элемент преобразовывается с помощью указанной функции.
const b = [1, 2, 3, 4, 5];
const squaredArray = b.map(function(item) {
  return item * item;
});
console.log(squaredArray); // Output: [1, 4, 9, 16, 25]


// 3. filter: Создает новый массив, содержащий все элементы, прошедшие проверку, заданную в указанной функции.
const c = [1, 2, 3, 4, 5];
const evenArray = c.filter(function(item) {
  return item % 2 === 0;
});
console.log(evenArray); // Output: [2, 4]


// 4. findIndex: Возвращает индекс первого элемента массива, который удовлетворяет условию, заданному в указанной функции.
const d = [1, 2, 3, 4, 5];
const index = d.findIndex(function(item) {
  return item === 3;
});
console.log(index); // Output: 2


// 5. reduce: Применяет указанную функцию к аккумулятору и каждому элементу массива (слева направо) для уменьшения его до одного значения.
const e = [1, 2, 3, 4, 5];
const sum = e.reduce(function(accumulator, item) {
  return accumulator + item;
}, 0);
console.log(sum); // Output: 15


// 6. some: Проверяет, удовлетворяет ли хотя бы один элемент массива условию, заданному в указанной функции.
const f = [1, 2, 3, 4, 5];
const hasEven = f.some(function(item) {
  return item % 2 === 0;
});
console.log(hasEven); // Output: true


// 7. every: Проверяет, удовлетворяют ли все элементы массива условию, заданному в указанной функции.
const g = [1, 2, 3, 4, 5];
const allEven = g.every(function(item) {
  return item % 2 === 0;
});
console.log(allEven); // Output: false
