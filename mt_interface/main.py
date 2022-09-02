# main.py
import nltk
from flask import request
from flask import jsonify
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    details = request.get_json()['details']

    # I just commented the code below for testing purposes

    # nltk.download('vader_lexicon')
    # from nltk.sentiment.vader import SentimentIntensityAnalyzer
    # sid = SentimentIntensityAnalyzer()
    # score = ((sid.polarity_scores(str(text))))['compound']

    # if(score > 0):
    #     label = 'This sentence is positive'
    # elif(score == 0):
    #     label = 'This sentence is neutral'
    # else:
    #     label = 'This sentence is negative'

    # TODO: (M. Yahia) right now I'm just returning the same text received from react
    # you have to replac the below 'details' variable with the translated one
    return({"translatedDetails": details})

if __name__ == "__main__":
    app.run(port='8088', threaded=False, debug=True)