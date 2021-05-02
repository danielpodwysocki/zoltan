FROM tiangolo/uwsgi-nginx-flask:python3.8
EXPOSE 80
ENV HOST_REGEXP .
ENV PROJECT_NUMBER default
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
COPY ./app /app
