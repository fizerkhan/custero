import os
import plivo

## Get pilvo configuration
PLIVO_AUTH_ID = os.getenv('PLIVO_AUTH_ID', '')
PLIVO_AUTH_TOKEN = os.getenv('PLIVO_AUTH_TOKEN', '')
PLIVO_NUMBER = os.getenv('PLIVO_NUMBER', '')
plivoApi = plivo.RestAPI(PLIVO_AUTH_ID, PLIVO_AUTH_TOKEN)

def send(destination_number):

  # Enter the SMS that you want to send
  text = "Welcome to Plivo!"
  message_params = {
        'src':PLIVO_NUMBER,
        'dst':destination_number,
        'text':text,
      }
  print plivoApi.send_message(message_params)
