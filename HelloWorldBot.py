
 from __future__ import print_function

import json
from flask import Flask, request
import requests


ACCESS_TOKEN = "EAAD0FIbuQqcBAKGQwe7ZB5xM2E9T2bHFg29YSZCCFZBUYF9XI7zQBk7HWsmVq84qvvC96lMKf37p7dfCWRMoQRkzMiDarOumdWvEWlNN2h8PuYrjAPoRcKBij6b6xQmL2zl9j5h2aLD0uWg91RY2OsY5KVD3CYp0rGDa5LCHgZDZD"
 
	
	


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
					
					reply(sender, "ma3lesh)
					return "ok"
				else:
					return "ok"
	return "ok"

if __name__ == '__main__':
    app.run(debug=True)
