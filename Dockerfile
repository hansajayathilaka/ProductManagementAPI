FROM python:3.10-alpine as base
LABEL authors="hansa"

RUN apk update
RUN python -m pip install --upgrade pip

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app/requirements.txt
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r /app/requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

WORKDIR /app
COPY . /app

FROM base as dev
ENV DEBUG=1
RUN chmod a+x ./entrypoint.dev.sh
CMD ["./entrypoint.dev.sh"]

FROM base as prod
ENV DEBUG=0
RUN chmod a+x ./entrypoint.sh
CMD ["./entrypoint.sh"]
