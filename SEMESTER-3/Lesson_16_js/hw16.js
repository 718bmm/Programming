// 1. length: Возвращает длину строки.
const a = "Hello, World!";
console.log(a.length); // Output: 13


// 2. toUpperCase: Преобразует все символы строки в верхний регистр.
const b = "Hello, World!";
console.log(b.toUpperCase()); // Output: HELLO, WORLD!


// 3. toLowerCase: Преобразует все символы строки в нижний регистр.
const c = "Hello, World!";
console.log(c.toLowerCase()); // Output: hello, world!


// 4. charAt: Возвращает символ по указанному индексу.
const d = "Hello, World!";
console.log(d.charAt(0)); // Output: H
console.log(d.charAt(7)); // Output: W


// 5. indexOf: Возвращает индекс первого совпадающего символа или подстроки.
const e = "Hello, World!";
console.log(e.indexOf("World")); // Output: 7


// 6. endsWith: Проверяет, оканчивается ли строка заданной подстрокой.
const f = "Hello, World!";
console.log(f.endsWith("World")); // Output: true
console.log(f.endsWith("Hello")); // Output: false


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
