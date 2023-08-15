

// 7. substring: Возвращает подстроку начиная с указанного индекса (включительно) и до указанного индекса (не включительно).
const g = "Hello, World!";
console.log(g.substring(0, 5)); // Output: Hello


// 8. split: Разделяет строку на массив подстрок на основе указанного разделителя.
const h = "Hello, World!";
console.log(h.split(" ")); // Output: ["Hello,", "World!"]


// 9. replace: Заменяет все совпадения подстроки на новое значение.
const i = "Hello, World!";
console.log(str.replace("World", "Universe")); // Output: Hello, Universe!


// 10. trim: Удаляет пробелы с начала и конца строки.
const j = "    Hello, World!    ";
console.log(str.trim()); // Output: Hello, World!


// 11. concat: Объединяет две строки.
const k = "Hello";
const l = "World!";
console.log(k.concat(", ", l)); // Output: Hello, World!


// 12. includes: Проверяет, содержится ли указанная подстрока в строке.
const m = "Hello, World!";
console.log(m.includes("World")); // Output: true
console.log(m.includes("Universe")); // Output: false