#!/usr/bin/env python
from flask import Flask ,render_template

def score_server(name):
    try:
        #get user score
        file_open = open(name , 'r+')
        user_score = file_open.read()
        file_open.close()

        return user_score

    except:
        return 'ERROR'

app = Flask(__name__)

@app.route('/')
def show_score():
    l_score = score_server('asa.txt')
    return render_template("html_score.html" , score = l_score)
    # score_server('asa.txt')

app.run(host='0.0.0.0', port=8777, debug=True)
