FROM python:3.8.0b3-alpine3.10
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN apk update && apk add axel && \
    rm -rf /var/lib/apt/lists/* && \
    rm /var/cache/apk/*
COPY . /usr/src/app
EXPOSE 80
CMD ["python", "api.py"]