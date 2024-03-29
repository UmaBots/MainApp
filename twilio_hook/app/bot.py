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
    body = 'Body'
    incoming_msg = request.values.get(body, '').lower()
    s = 'From'
    sender_id = request.values.get(s, '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    bot = 'bot_session0'
    bot_ = """Digite:
        SatoBot,
        VivaBot
        ou
        CBot
        """
    ok_ = 'ok!'
    sato_bot = 'SatoBot'
    viva_bot = 'VivaBot'
    c_bot = 'CBot'
    uma_bot = 'UmaBot'
    rasa_bot = 'rasa2bot'


    if incoming_msg.casefold() == sato_bot.casefold():
        session[bot] = sato_bot
        msg.body(ok_)
    elif incoming_msg.casefold() == viva_bot.casefold():
        session[bot] = viva_bot
        msg.body(ok_)
    elif incoming_msg.casefold() == c_bot.casefold():
        session[bot] = c_bot
        msg.body(ok_)
    elif incoming_msg.casefold() == uma_bot.casefold():
        session[bot] = uma_bot
        msg.body(ok_)
    elif incoming_msg.casefold() == rasa_bot.casefold():
        session[bot] = rasa_bot
        msg.body(ok_)

    elif bot in session:
        int1 = session[bot]
        if int1.casefold() == c_bot.casefold():
            resp = thelma(incoming_msg, sender_id)
        elif int1.casefold() == viva_bot.casefold():
            resp = viva(incoming_msg, sender_id)
        elif int1.casefold() == sato_bot.casefold():
            resp = sato(incoming_msg, sender_id)
        elif int1.casefold() == uma_bot.casefold():
            resp = uma(incoming_msg, sender_id)
        elif int1.casefold() == rasa_bot.casefold():
            resp = rasa2(incoming_msg, sender_id)
    else:
        msg.body(bot_)

    return str(resp)


def thelma(incoming_msg, sender_id):
    resp = MessagingResponse()
    msg = resp.message()
    var_i = {
        "sender": sender_id,
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


def uma(incoming_msg, sender_id):
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    var_i = {
        "sender": sender_id,
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


def sato(incoming_msg, sender_id):
    resp = MessagingResponse()
    msg = resp.message()
    var_i = {
        "sender": sender_id,
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

def viva(incoming_msg, sender_id):
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    var_i = {
        "sender": sender_id,
        "message": incoming_msg
    }
    webhook = 'http://viva:5005/webhooks/rest/webhook'
    requests_post = requests.post(webhook, json=var_i)
    json = requests_post.json()
    app.logger.info([json, var_i])
    cliente = MongoClient('mongo', 27017, username='root',
                          password='boquito_selma321')
    print(cliente['talk_store']['viva_talks'].insert_one(
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

def rasa2(incoming_msg, sender_id):
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    var_i = {
        "sender": sender_id,
        "message": incoming_msg
    }
    webhook = 'http://rasa2.0:5005/webhooks/rest/webhook'
    requests_post = requests.post(webhook, json=var_i)
    json = requests_post.json()
    app.logger.info([json, var_i])
    cliente = MongoClient('mongo', 27017, username='root',
                          password='boquito_selma321')
    print(cliente['talk_store']['rasa2.0_talks'].insert_one(
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


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)
