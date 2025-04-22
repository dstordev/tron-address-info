FROM python:3.11

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./src /app/src
COPY ./.env /app/.env

CMD ["fastapi", "run", "src/app.py", "--port", "8000"]
