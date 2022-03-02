from pythonisms.weapon_classes import Bazooka, SniperRifle, MachineGun

# squads is a dict with the names of the squad as the key
# Note: If you pass a squad into the Army on init the value it currently breaks iter
class Army:
  def __init__(self, name, squads = None):
    self.name = name
    self.total_army = {} if squads is None else squads

  def add_squads(self, squad):
    self.total_army[squad.name]=squad

  def __iter__(self):
    def value_generator():
      for squad in self.total_army:
        yield self.total_army[squad]
    
    return value_generator()

  def army_health(self):
    output = 0
    for squad in self:
      output += squad.squad_health()
    return output

  def __str__(self):
    output = f"{self.name}: "
    for squad in self:
      output += f"Squad:{str(squad)}\n"
    return output

class Squad:
  def __init__(self,name, soldiers = None):
    self.name = name
    self.soldiers = {} if soldiers is None else soldiers
    self.co = None

  def __iter__(self):
    def value_generator():
      for soldier in self.soldiers:
        yield self.soldiers[soldier]
    
    return value_generator()

  def add_soldiers(self, soldier):
    self.soldiers[soldier.name] = soldier

  def squad_health(self):
    ouput = 0
    for soldier in self:
      ouput +=soldier.health
    return ouput

  def __str__(self):
    output = f"{self.name} with: "
    for soldier in self:
      output += f"{soldier.name} "
    return output[:-1]

class Soldier:
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return self.name

class HeavyWeapons(Soldier):
  def __init__(self, name):
    super().__init__(name)
    self.weapon = Bazooka
    self.cry = "Its a big boom"
    self.health = 150

class Sniper(Soldier):
  def __init__(self, name):
    super().__init__(name)
    self.weapon = SniperRifle
    self.cry = "HEADSHOT"
    self.health = 75

class MachineGunner(Soldier):
  def __init__(self, name):
    super().__init__(name)
    self.weapon = MachineGun
    self.cry = "Say Hello to My little friend"
    self.health = 100