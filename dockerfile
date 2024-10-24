FROM python:latest

COPY . /app

RUN apt-get update \
    && apt-get upgrade \
    && pip install --no-chache-dir -r requirements.txt

EXPOSE 81

ENTRYPOINT ["python", "./app/standart.py"]
