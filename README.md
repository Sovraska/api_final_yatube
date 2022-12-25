# Api_final_yatube
���� **Backend** ������ ��� �������������� � **Frontend** ������ �������.  

� �������� �� ����� ��� ��������� � **���� ������** � ��������� ������ ����������.

�� ����� ����������� ��� ��� �� ����� ������ backend  
� ����� ����� ������������� ���� ������ �� **Frontend** :smile:




# ��� ��������� ������:
����������� ����������� � ������� � ���� � ��������� ������:

`git clone git@github.com:Sovraska/api_final_yatube.git`

`cd yatube_api`

������� � ������������ ����������� ���������:

`python -m venv venv`

`source venv/bin/activate`

���������� ����������� �� ����� requirements.txt:

`python -m pip install --upgrade pip`

`pip install -r requirements.txt`

��������� ��������:

`python manage.py migrate`

��������� ������:

`python manage.py runserver`

# ��� ����� ���������� �� ������� �������� � API ?
��������, ����� ������� ������� ����� ���������� [������������](http://127.0.0.1:8000/redoc/).

�� � ������� ��������� ��������.

GET http://127.0.0.1:8000/api/v1/posts/  
<sub> ������ ���� ������</sub>

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
<sub>�������� �����</sub>

    {
        "text": "string",
        "image": "string",
        "group": 0
    }

POST http://127.0.0.1:8000/api/v1/jwt/create/  
<sub> ��������� JWT ������</sub>

    {
        "username": "string",
        "password": "string"
    }