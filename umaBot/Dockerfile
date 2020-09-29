FROM python:3.7

# COPY global.yml /root/.config/rasa/global.yml
COPY . /bot
WORKDIR /bot
RUN pip install rasa && pip install rasa-x --extra-index-url https://pypi.rasa.com/simple
CMD export RASA_X_PASSWORD="boquito098"  && rasa train && rasa run 
EXPOSE 5005 5002
