# pythonのTags名を指定。
FROM python:3.10-alpine3.15

WORKDIR /backend

COPY ./requirements.txt /backend/requirements.txt

RUN apk add --no-cache postgresql-libs \
    && apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev \
    && python3 -m pip install -r /backend/requirements.txt --no-cache-dir \
    && apk --purge del .build-deps

COPY . /backend
