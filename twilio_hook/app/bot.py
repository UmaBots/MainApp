from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/', methods=['GET'])
def bot_iii():
    return 'Oki...'

@app.route('/umabot', methods=['POST'])
def bot_i():
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
    cliente = MongoClient('mongo', 27017,username='root', password='boquito_selma321')
    print(cliente['sato_tracker_store']['sato_talks'].insert_one({'i':request.values,'o': json}).inserted_id)
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

@app.route('/satobot', methods=['POST'])
def bot_ii():
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
    cliente = MongoClient('mongo', 27017,username='root', password='boquito_selma321')
    print(cliente['sato_tracker_store']['sato_talks'].insert_one({'i':request.values,'o': json}).inserted_id)
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
