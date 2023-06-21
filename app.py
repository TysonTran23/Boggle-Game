import time

from boggle import Boggle
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)
app.debug = True

#This is a instance 
boggle_game = Boggle()

@app.route('/')
def show_boggle():
    #Create the game board
    board = boggle_game.make_board()
    #Store board to session
    session['board'] = board

    return render_template('index.html', board=board, time=time.time())

@app.route('/guess')
def guess():
    #Grab word from get request
    word = request.args.get('guess')
    #Grab board from session
    board = session['board']
    #Function checks if word is valid/On the game board
    is_valid = boggle_game.check_valid_word(board, word)

    #Return "ok"/"not-on-board"/"not-word" as JSON to client side
    return jsonify({"result": is_valid})

@app.route('/game-over', methods = ['POST'])
def gameOver():

#Grab the score sent from Client-Side
    score = request.json['score']

#Grab the highscore/number of amount times played from session, if there is not any in the session, set them to 0
    highscore = session.get('highscore', 0)
    played_times = session.get('played_times', 0)

#If the score that was sent in was higher than the high score, set the new highscore.

    session['highscore'] = int(score) if int(score) > highscore else highscore
#Increment the amount of times played
    session['played_times'] = played_times + 1

#Return the new amount of times played/Send back updated highscool/Send back score
    return jsonify({"score": score, "highscore": session['highscore'], "played": played_times})


