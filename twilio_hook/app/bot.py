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
    session_values_get = None
    if 'bot' in session:
        session_values_get = session['bot']
        app.logger.info(['22 >>', session_values_get, incoming_msg])
    else:
        session['bot'] = incoming_msg
    resp = MessagingResponse()
    msg = resp.message()
    msg.body("""digite:
    1 - SatoBot
    2 - VivaBot
    3 - ClesioBot
    """)
    return str(resp)


@app.route('/thelma', methods=['POST'])
def thelma():
    app.logger.info(request.values)
    incoming_msg = request.values.get('Body', '').lower()
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


@app.route('/uma', methods=['POST'])
def uma():
    app.logger.info(request.values)
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
# twilio_hook_1    | [2020-09-30 00:15:53,856] INFO in bot: [[{'recipient_id': 'Rasa', 'text': 'Aqui está algo para animá-lo:'}, {'recipient_id': 'Rasa', 'image': 'https://i.imgur.com/nGF1K8f.jpg'}, {'recipient_id': 'Rasa', 'text': 'Isso ajudou você?'}], {'sender': 'Rasa', 'message': 'não muito bem'}]
        image = 'image'
        if image in j:
            app.logger.info(j)
            msg.media(j[image])

    return str(resp)


@app.route('/sato', methods=['POST'])
def sato():
    app.logger.info(request.values)
    incoming_msg = request.values.get('Body', '').lower()
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
        # image = 'image'
        # if image in j:
        #     msg.media(image)  # não funfa ainda TODO
    return str(resp)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)
