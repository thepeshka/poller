FROM python:3.6

ENV PYTHONPATH /var/www
ENV DJANGO_SETTINGS_MODULE poller.settings

COPY ./requirements.txt /var/www/requirements.txt
WORKDIR /usr/local/lib/python3.6
RUN pip install -r /var/www/requirements.txt
WORKDIR /var/www
COPY ./src /var/www
COPY ./deploy/entrypoint_python.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT /entrypoint.sh