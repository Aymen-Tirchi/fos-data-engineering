FROM python:3.9-alpine

RUN apk add --no-cache dcron gcc gfortran musl-dev lapack-dev

WORKDIR /app

COPY cities.json /app

COPY . .

RUN apk add --no-cache --virtual .build-deps build-base && \
    apk add --no-cache lapack && \
    ln -s /usr/include/locale.h /usr/include/xlocale.h && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del .build-deps

RUN mkdir -p /etc/cron.d/
RUN echo "*/10 * * * * /usr/local/bin/python /app/etl.py >> /var/log/cron.log 2>&1" >> /etc/cron.d/etl-cron

RUN chmod 0644 /etc/cron.d/etl-cron

RUN crontab /etc/cron.d/etl-cron

RUN touch /var/log/cron.log

CMD crond && tail -f /var/log/cron.log
