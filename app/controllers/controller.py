from app import app
from flask import render_template
from app.models.player import Player
from app.models.player_choice import players
from app.models.game import Game



# @app.route('/player_1/player_2') # where does this / refer to?
# def index():
#     player_1.choice = 
#     player_2.choice = 
#     return render_template("index.html", title = "home", players=players)

@app.route('/player_1/<player_1_name>/<player_1_guess>/player_2/<player_2_name>/<player_2_guess>') # where does this / refer to?
def index(player_1_name, player_1_guess, player_2_name, player_2_guess):
    # # player_1
    player_1 = Player(player_1_name, player_1_guess)
    player_2 = Player(player_2_name, player_2_guess)
    the_game = Game()
    result = the_game.play(player_1, player_2)
    return render_template("index.html", result=result, title="Skies")





#@app.route('/rock/rock') # so flask returns rock/rock and the return function to the server?
#def draw():
 #       return "Its a draw"

#@app.route('/rock/paper') #test inputs are made in html as python code?
#def rock_wins():
 #   return "rock wins"