// Events Task

// Mouse
// 1. mousedown - Срабатывает при нажатии кнопки мыши на элементе.
element.addEventListener('mousedown', function(event) {
  console.log('Mouse Down');
});


// 2. mouseup - Срабатывает при отпускании кнопки мыши, после ее нажатия на элементе.
element.addEventListener('mouseup', function(event) {
  console.log('Mouse Up');
});


// 3. mouseover - Срабатывает, когда указатель мыши перемещается на элемент.
element.addEventListener('mouseover', function(event) {
  console.log('Mouse Over');
});


// 4. mouseout - Срабатывает, когда указатель мыши покидает элемент.
element.addEventListener('mouseout', function(event) {
  console.log('Mouse Out');
});


// Keyboard
// 1. keydown - Срабатывает при нажатии клавиши на клавиатуре.
document.addEventListener('keydown', function(event) {
  console.log('Key Down: ' + event.key);
});


// 2. keyup - Срабатывает при отпускании клавиши на клавиатуре.
document.addEventListener('keyup', function(event) {
  console.log('Key Up: ' + event.key);
});


// 3. keypress - Более устаревшее событие, срабатывает при нажатии клавиши на клавиатуре и возвращает символ (для символических клавиш). Однако это событие может быть неработоспособно с некоторыми клавишами.
document.addEventListener('keypress', function(event) {
  console.log('Key Press: ' + event.key);
});


// Ball Task
const ball = document.getElementById("ball");
const defaultPosition = ball.offsetTop;
const jumpHeight = 200;

function jump(event) {
    if (event.code === "Space" || event.code === "Enter" || event.code === "UpArrow") {
        ball.style.top = (defaultPosition - jumpHeight) + "px";
        
        setTimeout(function() {
            ball.style.top = defaultPosition + "px";
        }, 1000);
    }
}

document.addEventListener("keydown", jump);




// Blog Task 
const userData = new URLSearchParams(window.location.search);
let mail = document.querySelector("h1");
mail.innerHTML = userData.get("mail");

// Создать личный блог
// 1. Главная страница блога должна имеет: | +/-
//    1. Информацию о Вас | +
//    2. Панель навигации по сайту | -
//    3. Ваши социальные сети | +
//    4. Статьи, которые вы написали (можно создать одну и копировать для вида) | +
//    5. Форму для регистрации мейла | +
//    6. Пагинация | -
//    7. Всё что вы бы хотиели включить | ?
// 2. Страница статьи (создайте одну такую страницу и продублируйте) | +
// 3. Отдельная страница О Вас/About me | +
// 4. Страница для создания Статьи: | +
//     1. должна содержать форму (form) для создании статьи (название, текст статьи, кто создал, когда создал) | +
// 5. Любая другая страница по вашему желанию | ?





