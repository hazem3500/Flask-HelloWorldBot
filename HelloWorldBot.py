from flask import Flask, request
from wit import Wit
import requests
import json
import traceback
import random

app = Flask(__name__)

client = Wit(access_token="2K7GXJSRTF7B5ZB74PNZBZQPGFYIIRKC")
token = "EAAD0FIbuQqcBAB7Eiz2Ng4jVHV4emNRC6kO8sTmJXoPFYqlsS3Namifdxw5GlvhZClnTVf2R6LLritVbXFuHtgU3OLD0X4yvdZAQEs4RixuKpmfaeT0pz45Yps5D1ZAWGD66eTLMfxghXowtRjxPJWf3WZALfZAlNvJBHFqwRPQZDZD"

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
  if request.method == 'POST':
    try:
      data = json.loads(request.data)
      text = data['entry'][0]['messaging'][0]['message']['text'] # Incoming Message Text
      sender = data['entry'][0]['messaging'][0]['sender']['id'] # Sender ID
      resp = client.converse(sender, text, {})
      payload = {'recipient': {'id': sender}, 'message': {'text': resp ['msg']}} # We're going to send this back
      r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + token, json=payload) # Lets send it
    except Exception as e:
      print traceback.format_exc() # something went wrong
  elif request.method == 'GET': # For the initial verification
    if request.args.get('hub.verify_token') == 'banana':
      return request.args.get('hub.challenge')
    return "Wrong Verify Token"

if __name__ == '__main__':
  app.run(debug=True)
