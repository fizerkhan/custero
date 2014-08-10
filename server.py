import os
from flask import Flask
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

if __name__ == '__main__':
  app.run()
