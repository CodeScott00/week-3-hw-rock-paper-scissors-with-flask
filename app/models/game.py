
from app.models.player import Player

class Game:

  def __init__(self): 
    pass

  def play(self,player_1,player_2):
    if player_1.choice.lower() == "rock" and player_2.choice.lower() == "rock":
      return None 
    if player_1.choice.lower() == "rock" and player_2.choice.lower() == "paper":
      return player_2.name + " wins!"
    if player_1.choice.lower() == "rock" and player_2.choice.lower() == "scissors":
      return player_1.name + " wins!"
    if player_1.choice.lower() == "paper" and player_2.choice.lower() == "papper":
      return None
    if player_1.choice.lower() == "paper" and player_2.choice.lower() == "scissors":
      return player_2.name + " wins!"
    if player_1.choice.lower() == "scissors" and player_2.choice.lower() == "scissors":
      return None 

      #add 3 more iterations