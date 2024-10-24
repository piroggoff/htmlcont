FROM python:latest

COPY . /app

WORKDIR /app

RUN apt-get update \
    && apt-get upgrade \
    && pip install -r requirements.txt

EXPOSE 81

ENTRYPOINT ["python", "/app/standart.py"]
