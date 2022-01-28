from random import random


class Weapon:
  def __init__(self) -> None:
      self.damage = 0
      self.reload = 0

class Bazooka(Weapon):
  def __init__(self) -> None:
    self.type = "Bazooka"
    self.damage = 50
    self.reload = 5

class SniperRifle(Weapon):
  def __init__(self) -> None:
    self.type = "Sniper Rifle"
    self.damage = 100 if random() > .5 else 5
    self.reload = 3

class MachineGun(Weapon):
  def __init__(self) -> None:
    self.type = "Machine Gun"
    self.damage = 10
    self.damage = 1