#FROM  python:3.7
#RUN apt-get update
#RUN apt-get install -y libpq-dev python-dev
#
#ADD srcs /app
#COPY srcs/requirements.txt /app
#RUN pip install -r /app/requirements.txt
#VOLUME ["/app"]
#
#WORKDIR /app
#ENTRYPOINT ["uwsgi"]
#CMD ["--socket", "0.0.0.0:8000", "--protocol=http", "-w", "main:app"]

FROM tiangolo/uwsgi-nginx:python3.7

ENV UWSGI_INI /application/uwsgi.ini

COPY ./srcs /application
RUN pip install -r /application/requirements.txt

WORKDIR /application
