from helper.openai_api import chat
from helper.twillio import send_message
from flask import Flask, request
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)


@app.route('/')
def home():
    return '200'


@app.route('/twilio/receiveMessage', methods=['POST'])
def receiveMessage():
    try:
        # Extract incomng parameters from Twilio
        message = request.form['Body']
        sender_id = request.form['From']
        result = chat(message)
        if result['status'] == 1:
            send_message(sender_id, result['response'])
    except:
        pass
    return 'OK', 200
