
from flask import Flask, request
from flask_cors import CORS
from twilio.twiml.voice_response import VoiceResponse, Gather
from utils.stories import load_story
from utils.call import answer_call,read_story
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

CORS(app)

@app.route("/voice", methods=['GET','POST'])
def answer():
    return answer_call()

@app.route("/story", methods=['GET','POST'])
def read():
    if 'Digits' in request.values:
        choice = request.values['Digits']
        if choice <= '3':
            return read_story(choice)
        else:
            return read_story()

 
if __name__ == "__main__":
    app.run(debug=True)