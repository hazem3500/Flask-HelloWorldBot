from __future__ import print_function

import os
import sys
import json
from flask import Flask, request
import requests


from wit import Wit


CLIENT_ACCESS_TOKEN = '7S2D2JZ4EGCIGC6GUXATTOYFVBSVQ65F'
ACCESS_TOKEN = "EAAD0FIbuQqcBAEDdtxtURYnmZArL4Xu1GaokZBZBk6UTM6vqufcYGEvd5q1OfZAicWBScBzMcUfakmsZCcFb71imQSP3nrFDezqgdyZASOmH9JA020ZBCKcbpikLjQGMkkewEWf5cHmoeoiioZC8EAEtuepQRwjeMqinMWX3sWT7CgZDZD"







app = Flask(__name__)


#
#def send(request, response):
#    """
#    Sender function
#    """
#    # We use the fb_id as equal to session_id
#    fb_id = request['session_id']
#    text = response['text']
#    # send message
#    reply(fb_id, text)
#

def reply(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg}
    }
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    return resp.content


@app.route('/', methods=['GET'])
def handle_verification():
    return request.args['hub.challenge']


@app.route('/', methods=['POST'])
def handle_incoming_messages():
	data = request.json
	if data['object'] == "page":
		for entry in data['entry']:
			pageID = entry['id']
			for msg in entry['messaging']:
				if msg['message']:
					sender = msg['sender']['id']
					message = msg['message']['text']


					context0 = {}
					response = client.converse(sender, message, context0)


					reply(sender, str(response['msg']))
					return "ok"
				else:
					return "ok"
	return "ok"
#
#
#actions = {
#    'send': send,
#}


client = Wit(access_token=CLIENT_ACCESS_TOKEN)

if __name__ == '__main__':
    app.run(debug=True)
