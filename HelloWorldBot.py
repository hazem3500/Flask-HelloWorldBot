from flask import Flask, request
import requests
import json
import traceback
import random
app = Flask(__name__)

token = "EAAD0FIbuQqcBAAZBr6ZAvNEcLwCIjF6mQ0QDst9pZCV3T1UohpBCiP1SH4e6nE7bHXPTttLGPzZBzfpWSrt3umJ4dp89ZBOVN9MZCCNZCEZAkhKXt5M95lTvHCEuW6sCsdmNr3ZArOu7JRXxWYO2x0MYTvplaW4Lfkv15CtqoOyPc5QZDZD"

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
