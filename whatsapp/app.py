import os
import requests
from flask import Flask, request
import dialogflow_v2 as dialogflow
from twilio.twiml.messaging_response import MessagingResponse

# INSERT JSON key's PATH
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "jokes-bupppg-d3f2d8a46c85.json"

# INSERT YOUR PROJECT ID
dialogflow_session_client = dialogflow.SessionsClient()
PROJECT_ID = "jokes-bupppg"

def detect_intent_from_text(text, session_id, language_code='en'):
    session = dialogflow_session_client.session_path(PROJECT_ID, session_id)
    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = dialogflow_session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result

def fetch_reply(query, session_id):
    response = detect_intent_from_text(query, session_id)
    return response.fulfillment_text

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming message"""
    # Fetch the message
    msg = request.form.get('Body')
    phone_no = request.form.get('From')
    reply = fetch_reply(msg, phone_no)

    # Create reply
    resp = MessagingResponse()

    #resp.message(reply)
    resp.message(format(reply))

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
