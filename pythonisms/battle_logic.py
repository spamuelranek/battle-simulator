import sys
from pythonisms.people_classes import (
  Army,
  Squad,
  Sniper,
  HeavyWeapons,
  MachineGunner
)


class Game:
  
  def __init__(self):
    self.phrase_bank = {"start":"Would you like to play a game? y/n",
    "play":"So glad you can join us today!",
    "army_name":"Please pick a name for you army.",
    "created": "has been created",
    "buy_or_fight": "would you like to grow your army or go to the battlefield? buy/fight"}

  def starting_squad(self):
    mark = Sniper("Mark")
    tammy = HeavyWeapons("Tammy")
    ronix = MachineGunner("Ronix")
    peeps = {mark.name:mark, tammy.name:tammy, ronix.name:ronix}
    return Squad("Monkey Brains", peeps)


  def start_game(self):
    print(self.phrase_bank["start"])
    response = input('> ')
    response = self.input_validation_for_quit(response)
    if response == 'y':
      self.play_game()
    elif response == 'n':
      print("Thanks for your time")


  def play_game(self):
    print(self.phrase_bank["play"])
    print(self.phrase_bank["army_name"])
    response = input('> ')
    response = self.input_validation_for_quit(response)
    player_army = Army(response)
    player_army.add_squads(self.starting_squad())
    print(str(player_army), self.phrase_bank["created"])
    while player_army.army_health() > 0:
      print(f"Leader of {player_army.name}, ", self.phrase_bank["buy_or_fight"])
      response = input('> ')
      response = self.input_validation_for_quit(response)
      if response == "buy":
        self.shop()
      elif response == "battle":
        self.battle()    

  def input_validation_for_quit(self,response):
    if response == "q":
      sys.exit()
    else:
      return response

  def shop(self):
    pass

  def battle(self):
    pass