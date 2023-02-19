Onboarding

### Технологии:
- Django 4.0.2
- Python 3.10.4
- HTML, CSS (Tailwind)
- SQLlite

Функционал:
-Авторизация
-Возможность добавлять сотрудников через админку Django
-Просмотр новостей

Демо - https://cloud.mail.ru/public/s2z4/DtbqtFtU1 


Установка:
--
```
$ git clone https://github.com/qvog/onboarding_hackathon.git
$ cd onboarding_hackathon
$ pip install -r requirements.txt
```

> Сделайте настройку собственной базы данных! 

Миграции и создание супер-пользователя.
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

> Используйте адрес: http://127.0.0.1:8000/ (Для проверки)
