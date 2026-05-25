Веб-приложение для бронирования рабочих мест «CoSpace»

Итоговый проект по программе «Python-разработчик».



Как запустить проект локально:

1. Установить зависимости:

"python -m pip install -r requirements.txt"

&#x09;Если выдает ошибку, можно использовать прямой путь:
	"\& "$env:LOCALAPPDATA\\Programs\\Python\\Python313\\python.exe" -m pip install -r requirements.txt"

2. Запустить веб-сервер:

"python -m uvicorn main:app --reload"

&#x09;Если выдает ошибку, можно использовать прямой путь:

&#x09;"\& "$env:LOCALAPPDATA\\Programs\\Python\\Python313\\Scripts\\uvicorn.exe" main:app --reload"

После запуска интерактивная документация API (Swagger) будет доступна по адресу: http://127.0.0.1:8000/docs

3. Запуск автоматических тестов:

"python -m pytest"

&#x09;Если выдает ошибку, можно использовать прямой путь:

&#x09;"\& "$env:LOCALAPPDATA\\Programs\\Python\\Python313\\python.exe" -m pytest"

