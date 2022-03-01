from urllib import response
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
    "created": "has been created"}

  def starting_squad(self):
    mark = Sniper("Mark")
    tammy = HeavyWeapons("Tammy")
    ronix = MachineGunner("Ronix")
    peeps = {mark.name:mark, tammy.name:tammy, ronix.name:ronix}
    return Squad("Monkey Brains", peeps)


  def start_game(self):
    print(self.phrase_bank["start"])
    response = input('> ')
    if response == 'y':
      self.play_game()
    elif response == 'n':
      print("Thanks for your time")


  def play_game(self):
    print(self.phrase_bank["play"])
    print(self.phrase_bank["army_name"])
    response = input('> ')
    player_army = Army(response)
    player_army.add_squads(self.starting_squad())
    print(str(player_army), self.phrase_bank["created"])
