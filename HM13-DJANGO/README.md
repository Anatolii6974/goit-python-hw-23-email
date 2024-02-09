Домашнє завдання №13
Друга частина 

Налаштовуємо параметри електронної пошти
quotes_scrape/quotes_scrape/settings.py

Під час реєстрації додаємо поле email
quotes_scrape/users/templates/users/signup.html
quotes_scrape/users/forms.py

Додаємо маршрути
quotes_scrape/users/urls.py
quotes_scrape/users/templates/users/login.html

Представлення для скидання пароля
quotes_scrape/users/views.py
quotes_scrape/users/templates/users/password_reset.html
quotes_scrape/users/templates/users/password_reset_email.html
quotes_scrape/users/templates/users/password_reset_subject.txt

Представлення успішного відправлення листа
quotes_scrape/users/templates/users/password_reset_done.html

Скидання пароля
quotes_scrape/users/templates/users/password_reset_confirm.html

Представлення успішного підтвердження
quotes_scrape/users/templates/users/password_reset_complete.html

Змінні середовища Django
.env


Для роботи проекта необхідний файл /quotes_scrape/.env зі змінними оточення. Створіть його з таким вмістом і підставте свої значення.

Запуск застосунку

cd quotes_scrape -> poetry run python manage.py runserver







