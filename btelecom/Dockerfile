FROM python:3.13.0a4-alpine3.19
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SECRET_KEY django-insecure-j)mqy_c^ti0tkuz(yvfx*-$eteoen#1(l&y&vg&kn%k4$g@5y+
ENV MYSQL_ENGINE django.db.backends.mysql
ENV MYSQL_DATABASE bezerratelecom
ENV MYSQL_USER dbadmin
ENV MYSQL_PASSWORD QDVqrPJ&6wt1YqCe
ENV MYSQL_HOST localhost
ENV MYSQL_PORT 3306
RUN mkdir -p /opt/sites/btelecom
WORKDIR /opt/sites/btelecom
# Installing OS Dependencies
RUN apk update && apk upgrade -l && apk add --no-cache sqlite mysql-client mariadb-connector-c-dev gcc musl-dev python3-dev libjpeg-turbo-dev zlib-dev
RUN python --version
RUN pip install -U pip setuptools && \
    pip install mysqlclient && \
    pip install Pillow && \
    pip install django
ADD . /opt/sites/btelecom/
# Django service
EXPOSE 80