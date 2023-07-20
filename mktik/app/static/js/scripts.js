function executeQuery() {
var ajax = new XMLHttpRequest();
ajax.open('GET', 'http://127.0.0.1:8000/addr_lst');
ajax.setRequestHeader("X-Requested-With", "XMLHttpRequest");
ajax.send();



ajax.onload = function() {
        if (ajax.readyState == 4) {

            if (ajax.status == 200 || ajax.status == 304) {
                // код при успешном запросе
                document.querySelector('.result').textContent = ajax.response; // ответ сервера
            } else {
                document.querySelector('.result').textContent = "Нет связи с сервером"
                // код при ошибке
            }
        }
    }
ajax.onerror = function() {
    document.querySelector('.result').textContent = "Error";

    }
    setTimeout(executeQuery, 15000);
}

$(document).ready(function() {
  // run the first time; all subsequent calls will take care of themselves
  setTimeout(executeQuery, 5000);
});

