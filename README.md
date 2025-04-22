# tron-address-info

### Запуск через docker

1. Впишите свои данные в `.env.example` и переименуйте его в `.env`
2. Соберите контейнеры: `docker compose build`
3. Поднимите их: `docker compose up`
4. Документация API будет распологаться по адресу `http://127.0.0.1:8000/docs`

### Запуск через python

*Вам потребуется запущенный сервер postgres*

1. Впишите свои данные в `.env.example` и переименуйте его в `.env`
2. Создайте виртуальное окружение: `python3 -m venv .venv`
3. Активируйте его (команда для Linux): `. .venv/bin/activate`
4. Установите зависимости: `pip install -r requirements.txt`
5. Запустите сервер: `fastapi run src/app.py --port 8000`
6. Документация API будет распологаться по адресу `http://127.0.0.1:8000/docs`
