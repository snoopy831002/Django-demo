FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /django-files
WORKDIR /django-files
RUN git clone https://github.com/snoopy831002/Django-demo.git
RUN pip install Django
#RUN django-admin startproject mysite
#ENTRYPOINT tail -f /dev/null
ENTRYPOINT python Django-demo/djangosite/manage.py runserver 0.0.0.0:7777
