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
    "buy_or_fight": "would you like to grow your army or go to the battlefield? buy/fight",
    "shop_welcome": "Welcome to the WAR shop. Here you can train new soliders or whole new squads.",
    "shop_options": """ 'Train a Sniper'    100 credits
 'Train a MachineGunner'    100 credits
 'Train a HeavyWeapons'   100 credits""",
    "shop_not_enough_money": "Sorry your credit amount is too low to pay for this option.",
    "train_solider_name": "What is the name of the Solider?",
    "train_solider_squad": "Which squad would you liked add this solider to?",
    "choose_a_valid_squad": "Please select from the available squads"}

    self.battle_phrase_bank = {"battle_welcome" : """Welcome to the battle arena.
This is where you will find out if you have the best army and tatics.
There will be 10 levels to master
You may retreat at any time, but it will cost you 100 credits.
If you do not have 100 credits then it comes to a coin flip.
The rest of the instructions will be presented as you go along."""}

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
        self.shop(player_army)
      elif response == "fight":
        self.battle(player_army)    

  def input_validation_for_quit(self,response):
    if response == "q":
      sys.exit()
    else:
      return response

  def input_validation_leave_shop(self,response, shop_status):
    if response == "leave shop":
      shop_status = False
      return shop_status

    return shop_status


  def shop(self, player_army):
    in_shop = True
    solider_training_options = {'Train a Sniper': "sniper",
    'Train a MachineGunner': "machinegunner",
    'Train a HeavyWeapons' : "heavyweapons"}
    store_pricing = {'Train a Sniper' : 100,
    'Train a HeavyWeapons' : 100,
    'Train a MachineGunner' : 100}

    print(self.phrase_bank["shop_welcome"])

    while in_shop:

      print(f"{player_army.name} has {player_army.credits} credits")
      print(self.phrase_bank["shop_options"])

      response = input('> ')
      response = self.input_validation_for_quit(response)
      in_shop = self.input_validation_leave_shop(response,in_shop)

      if response in store_pricing.keys() and player_army.credits >= store_pricing[response]:
        player_army.credits = player_army.credits - store_pricing[response]

        if response in solider_training_options.keys():
          self.train_solider(solider_training_options[response], player_army)
      elif response in store_pricing.keys():
        print(self.phrase_bank["shop_not_enough_money"])


  def train_solider(self, type, player_army):

    solider_types = {"sniper": Sniper, 
    "machinegunner": MachineGunner, 
    "heavyweapons": HeavyWeapons}

    chosen_type = solider_types[type]

    print(self.phrase_bank["train_solider_name"])

    response = input('> ')
    response = self.input_validation_for_quit(response)

    new_solider = chosen_type(response)
    print(f"{new_solider.name} uses:")
    print(f"{new_solider.weapon.type} and")
    print(f"has {new_solider.health} health")

    print(self.phrase_bank["train_solider_squad"])

    squad_names = "Squads available: "
    for squad in player_army:
      squad_names += f"{squad.name} "

    print(squad_names)

    chose_a_valid_squad = False
    while not chose_a_valid_squad:
      response = input('> ')
      response = self.input_validation_for_quit(response)

      chosen_squad = player_army.total_army.get(response)
      if chosen_squad:
        chosen_squad.add_soldiers(new_solider)
        print(str(chosen_squad))
        return player_army
      print(self.phrase_bank["choose_a_valid_squad"])


  def battle(self, player_army):
    print(self.battle_phrase_bank["battle_welcome"])