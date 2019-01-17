FROM python:3.6

ENV PYTHONPATH /var/www
ENV DJANGO_SETTINGS_MODULE poller.settings

WORKDIR /var/www

COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt
COPY ./src /var/www