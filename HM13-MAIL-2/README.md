Домашнє завдання №13
Перша частина 

Змінюємо моделі та репозиторій 
Сервіс надсилання листів для верифікації 
Змінюємо роботу маршрутів 
 - Реєстрація користувача 
 - Аутентифікація користувача 
Підтвердження email 
Повторне надсилання листа 

Змінні середовища REST API
.env
conf/config.py

Обмеження кількості запитів для маршрутів контактів
  - "username": "master",
  - "email": "anatolii.perfilov@gmail.com",
  - "password": "123456"
src/routes/users.py 

Збереження файлів у хмарі

Для роботи проекта необхідний файл ./.env зі змінними оточення. Створіть його з таким вмістом і підставте свої значення.






poetry run docker run --name email_app -p 5432:5432 -e POSTGRES_PASSWORD=751953 -d postgres
937f6f417c02d9a6865f158c32a1fbf2a0ae9ccd14aade27f050ee52ab3bc981
poetry run docker-compose up -d
poetry run uvicorn main:app --host localhost --port 8000 --reload






