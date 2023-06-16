from boggle import Boggle
from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension



app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = "secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

#This is a instance 
boggle_game = Boggle()

@app.route('/')
def show_boggle():
    board = boggle_game.make_board()
    session['board'] = board


    return render_template('index.html', board=board)







