import os
from flask import Flask, render_template, request, redirect
import sms

app = Flask(__name__)
app.config['DEBUG'] = os.environ.get('DEBUG', False)

@app.route('/')
def hello():
  return 'Hello World!'

@app.route('/sms')
def sendSMS():
  sms.send("919884364132")
  return 'Message sent!'

@app.route("/receive-sms", methods=['POST'])
def receive_sms():
  text = request.args.get('Text')
  _from = request.args.get('From')
  return 'Text received: %s - From: %s' % (text, _from)

if __name__ == '__main__':
  app.run()
