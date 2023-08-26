function count(array) {
    const countMap = {};
    array.forEach(element => {
      if (countMap[element]) {
        countMap[element] += 1;
      } else {
        countMap[element] = 1;
      }
    });
    return countMap;
  }
  
const array = ['james', 'james', 'john'];
const result = count(array);
console.log(result);  // { 'james': 2, 'john': 1 }




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




const a = [1, 2, 3, 4, 5];
a.forEach(function(item) {
  console.log(item);
});


const b = [1, 2, 3, 4, 5];
const squaredArray = b.map(function(item) {
  return item * item;
});
console.log(squaredArray);


const c = [1, 2, 3, 4, 5];
const evenArray = c.filter(function(item) {
  return item % 2 === 0;
});
console.log(evenArray);


const d = [1, 2, 3, 4, 5];
const index = d.findIndex(function(item) {
  return item === 3;
});
console.log(index);


const e = [1, 2, 3, 4, 5];
const sum = e.reduce(function(accumulator, item) {
  return accumulator + item;
}, 0);
console.log(sum);


const f = [1, 2, 3, 4, 5];
const hasEven = f.some(function(item) {
  return item % 2 === 0;
});
console.log(hasEven);

const g = [1, 2, 3, 4, 5];
const allEven = g.every(function(item) {
  return item % 2 === 0;
});
console.log(allEven);