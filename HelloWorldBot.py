from flask import Flask, request
import requests
import json
import traceback
import random
import wit
app = Flask(__name__)

client = Wit(access_token=WIT_TOKEN)
token = "EAAD0FIbuQqcBAApqsesPj32dGKapNgI4cZCoHSZBZAb1k5ZCyl4AG4ix523O2GNo7lSSKJakon5yipEuyTRovoDfFBO2HQGZAAUQWtbjZC9WXoZBCMzhbxfsvtnSTbjnFC8iC0VOPKeQqkJ94BGZCUKW2aZA2MiZA24ENC4OgZAFTwdbQZDZD"

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
  if request.method == 'POST':
    try:
      data = json.loads(request.data)
      text = data['entry'][0]['messaging'][0]['message']['text'] # Incoming Message Text
      sender = data['entry'][0]['messaging'][0]['sender']['id'] # Sender ID
      payload = {'recipient': {'id': sender}, 'message': {'text': "Hello World"}} # We're going to send this back
      r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + token, json=payload) # Lets send it
    except Exception as e:
      print traceback.format_exc() # something went wrong
  elif request.method == 'GET': # For the initial verification
    if request.args.get('hub.verify_token') == 'banana':
      return request.args.get('hub.challenge')
    return "Wrong Verify Token"
  return "Hello World" #Not Really Necessary

if __name__ == '__main__':
  app.run(debug=True)
