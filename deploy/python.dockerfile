FROM python:3.6

ENV PYTHONPATH /var/www
ENV DJANGO_SETTINGS_MODULE poller.settings

WORKDIR /var/www

COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt \
    && python /var/www/src/django/setup.py install
COPY ./src /var/www
COPY ./deploy/entrypoint_python.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT /entrypoint.sh