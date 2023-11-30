FROM python:3.10-slim-buster

RUN apt-get update && \
    apt-get install -y make

WORKDIR /src

EXPOSE 8080

COPY ../requirements /tmp/requirements

RUN pip install --no-cache-dir --upgrade -r /tmp/requirements/base.txt && \
    pip install --no-cache-dir --upgrade -r /tmp/requirements/dev.txt

COPY . . /src/

CMD ["make", "start"]