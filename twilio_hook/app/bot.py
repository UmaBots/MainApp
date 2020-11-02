from flask import Flask, request, session
import requests
from twilio.twiml.messaging_response import MessagingResponse
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = b'!gordalove6'


@app.route('/', methods=['GET'])
def oki0():
    return 'Oki...'


@app.route('/', methods=['POST'])
def oki1():
    app.logger.info(request.values)
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    bot = 'bot4'
    int1 = None
    try:
        int1 = int(incoming_msg)
    except:
        msg.body("""digite:
    1 - SatoBot
    2 - VivaBot
    3 - ClesioBot
    """)

    if bot in session:
        session_values_get = session[bot]
        i = session_values_get
        app.logger.info([isinstance(i, int), type(i)])
        if i == 3:
            return thelma(incoming_msg)
        elif i == 2:
            return viva(incoming_msg)
        elif i == 1:
            return sato(incoming_msg)
    elif isinstance(int1, int):
        session[bot] = int1

    app.logger.info([session_values_get, incoming_msg])
    return str(resp)


def thelma(incoming_msg):
    resp = MessagingResponse()
    msg = resp.message()
    var_i = {
        "sender": "Rasa",
        "message": incoming_msg
    }
    webhook = 'http://thelma:5005/webhooks/rest/webhook'
    requests_post = requests.post(webhook, json=var_i)
    json = requests_post.json()
    app.logger.info([json, var_i])
    cliente = MongoClient('mongo', 27017, username='root',
                          password='boquito_selma321')
    print(cliente['talk_store']['thelma_talks'].insert_one(
        {'i': request.values, 'o': json}).inserted_id)
    for j in json:
        print(j)
        text = 'text'
        if text in j:
            j_text_ = j[text]
            msg.body(j_text_)
        image = 'image'
        if image in j:
            app.logger.info(j)
            msg.media(j[image])
    return str(resp)


def uma():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    var_i = {
        "sender": "Rasa",
        "message": incoming_msg
    }
    webhook = 'http://uma:5005/webhooks/rest/webhook'
    requests_post = requests.post(webhook, json=var_i)
    json = requests_post.json()
    app.logger.info([json, var_i])
    cliente = MongoClient('mongo', 27017, username='root',
                          password='boquito_selma321')
    print(cliente['talk_store']['uma_talks'].insert_one(
        {'i': request.values, 'o': json}).inserted_id)
    for j in json:
        print(j)
        text = 'text'
        if text in j:
            j_text_ = j[text]
            msg.body(j_text_)
        image = 'image'
        if image in j:
            app.logger.info(j)
            msg.media(j[image])

    return str(resp)


def sato(incoming_msg):
    resp = MessagingResponse()
    msg = resp.message()
    var_i = {
        "sender": "Rasa",
        "message": incoming_msg
    }
    webhook = 'http://sato:5005/webhooks/rest/webhook'
    requests_post = requests.post(webhook, json=var_i)
    json = requests_post.json()
    app.logger.info([json, var_i])
    cliente = MongoClient('mongo', 27017, username='root',
                          password='boquito_selma321')
    print(cliente['talk_store']['sato_talks'].insert_one(
        {'i': request.values, 'o': json}).inserted_id)
    for j in json:
        print(j)
        text = 'text'
        if text in j:
            j_text_ = j[text]
            msg.body(j_text_)
    return str(resp)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)
