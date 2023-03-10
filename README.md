# Api_final_yatube
Этот **Backend** Создан для Взаимодействия с **Frontend** частью Проекта.  

В основном он нужен для обращения к **базе данных** И получения нужной информации.

Он может пригодиться тем кто не хочет писать backend  
а сразу хочет потренировать свои навыки во **Frontend** :smile:




# Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

`git clone git@github.com:Sovraska/api_final_yatube.git`

Создать и активировать виртуальное окружение:

`python -m venv venv`

`source venv/bin/activate`

Установить зависимости из файла requirements.txt:

`python -m pip install --upgrade pip`

`pip install -r requirements.txt`

Выполнить миграции:

`python manage.py migrate`

Запустить проект:

`python manage.py runserver`

# Где Можно Посмотреть на примеры запросов к API ?
Например, после запуска проекта можно посмотреть [Документацию](http://127.0.0.1:8000/redoc/).

Но я приведу несколько примеров.

GET http://127.0.0.1:8000/api/v1/posts/  
<sub> Список всех постов</sub>

    {
        "count": 123,
        "next": "http://api.example.org/accounts/?offset=400&limit=100",
        "previous": "http://api.example.org/accounts/?offset=200&limit=100",
        "results": [
            {
                "id": 0,
                "author": "string",
                "text": "string",
                "pub_date": "2021-10-14T20:41:29.648Z",
                "image": "string",
                "group": 0
            }
        ]
    }

POST http://127.0.0.1:8000/api/v1/posts/  
<sub>Отправка поста</sub>

    {
        "text": "string",
        "image": "string",
        "group": 0
    }

POST http://127.0.0.1:8000/api/v1/jwt/create/  
<sub> Получение JWT токена</sub>

    {
        "username": "string",
        "password": "string"
    }
