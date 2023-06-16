from boggle import Boggle
from flask import Flask, request, render_template, redirect, flash, session, jsonify
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
    board = boggle_game.make_board()
    session['board'] = board
    print('hi')
    return render_template('index.html', board=board)

@app.route('/guess')
def guess():
    word = request.args.get('guess')
    board = session['board']
    response = boggle_game.check_valid_word(board, word)

    return jsonify({'result': response})








