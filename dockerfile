FROM python:latest
RUN apt-get update \
    && apt-get upgrade \
    && pip install flask \
    && pip install markupsafe
COPY . /app
EXPOSE 5000
ENTRYPOINT ["python", "./app/standart.py"]
