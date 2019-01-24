FROM python:3.6

ENV PYTHONPATH /var/www
ENV DJANGO_SETTINGS_MODULE poller.settings

WORKDIR /var/www

COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt \
    && cp -r /var/www/src/django /usr/local/lib/python3.6/site-packages/django
COPY ./src /var/www
COPY ./deploy/entrypoint_python.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT /entrypoint.sh