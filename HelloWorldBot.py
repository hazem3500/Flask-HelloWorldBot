
 from __future__ import print_function

import json
from flask import Flask, request
import requests


ACCESS_TOKEN = "EAAD0FIbuQqcBAP3A0Qt0ibmc0x9L9W8t7ZCe47BmCoH72WctvkGF3UE5e1IMFoOaFPek9R3bidfimuZA5wdEZASlHQz4CKeZCUoB7r0ceIZBArQ1icEsQuP0X8ZApOCsq6vZBTp59mLSHoTEunQ8jZChxmdZC9XIOPn8ZBNg79oQfhDgZDZD"
 
	
	


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
					
					reply(sender, "ma3lesh")
					return "ok"
				else:
					return "ok"
	return "ok"

if __name__ == '__main__':
    app.run(debug=True)
