В данном проекте реализована бэкенд-часть веб-приложения на основе Django.

Приложение создано для ведения личного дневника.

В приложении реализованы технологии:

- Python
- Django
- PostgreSQL
- Redis
- Docker
- Docker-compose


Работа с приложением: 

- Клонируем приложение из github-a
- Активируем виртуально окружение 
- Устанавливаем зависимости pip install -r requirements.txt либо если у вас poetry то poetry install 
- Создаем и вносим данные в файл .env, все данные указанные в .env.sample 
- Создаем зависимости и применяем их 
- Устанавливаем Redis, запускаем командой redis-server 
- Запускаем django приложение командой python3 manage.py runserver. Если у вас poetry то используем команду python manage.py runserver


Запуск приложения через docker

В терминале введите команду docker-compose up -d --build
