FROM python:3.7

COPY global.yml /root/.config/rasa/global.yml
COPY . /bot
WORKDIR /bot
RUN pip install -U pip
RUN pip install rasa 
RUN pip install rasa-x==0.33.0 --extra-index-url https://pypi.rasa.com/simple
CMD rasa train & rasa run actions & rasa x &
EXPOSE 5005 5002 5055
