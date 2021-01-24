from app import app
from flask import render_template
from app.models.player import Player
from app.models.player_choice import players



@app.route('/player_1/player_2') # where does this / refer to?
def index():
    # player_1
    return render_template("index.html", title = "home", players=players)







#@app.route('/rock/rock') # so flask returns rock/rock and the return function to the server?
#def draw():
 #       return "Its a draw"

#@app.route('/rock/paper') #test inputs are made in html as python code?
#def rock_wins():
 #   return "rock wins"