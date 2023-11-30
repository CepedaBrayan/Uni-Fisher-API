FROM python:3.10-slim-buster

RUN apt-get update && \
    apt-get install -y make

WORKDIR /src

EXPOSE 8080

COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /tmp/requirements.txt

COPY . /app

CMD ["make", "start"]