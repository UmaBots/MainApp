FROM tiangolo/uwsgi-nginx-flask:python3.8

ENV LISTEN_PORT 5000
COPY ./app /app
WORKDIR /app
RUN pip install twilio flask requests pymongo
EXPOSE 5000