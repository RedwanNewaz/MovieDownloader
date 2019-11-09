FROM python:3.8.0b3-alpine3.10
WORKDIR /usr/src/app

RUN apk update && apk add axel

RUN apk --update add git less openssh && \
    rm -rf /var/lib/apt/lists/* && \
    rm /var/cache/apk/*

RUN git clone https://github.com/RedwanNewaz/MovieDownloader.git

COPY . /usr/src/app
RUN cd /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

RUN apk del git

EXPOSE 80
CMD ["python", "api.py"]
