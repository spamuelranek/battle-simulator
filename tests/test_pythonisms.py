from re import S
from pythonisms import __version__
from pythonisms.people_classes import Army, Squad, HeavyWeapons, Sniper, MachineGunner
import pytest


def test_version():
    assert __version__ == '0.1.0'

def test_is_army():
    assert Army

def test_is_squad():
    assert Squad

# @pytest.mark.skip()
def test_is_squad_subscript():
    squadmb = Squad("Monkey Brains")
    squadb = Squad("Brains")
    squadm = Squad("Monkey")
    small_army = Army("Test Army")
    small_army.add_squads(squadb)
    small_army.add_squads(squadm)
    small_army.add_squads(squadmb)
    actual = small_army.total_army["Brains"]
    expected = squadb
    assert actual == expected

def test_is_squad_iterable():
    squadmb = Squad("Monkey Brains")
    squadb = Squad("Brains")
    squadm = Squad("Monkey")
    small_army = Army("Test Army")
    small_army.add_squads(squadb)
    small_army.add_squads(squadm)
    small_army.add_squads(squadmb)
    actual = []
    for squad in small_army:
        actual.append(squad.name)
    expected = ["Brains", "Monkey", "Monkey Brains"]
    assert actual == expected

# now defunct due to changes to str on army and squad
@pytest.mark.skip()
def test_str_army_squad():
    squadmb = Squad("Monkey Brains")
    squadb = Squad("Brains")
    squadm = Squad("Monkey")
    small_army = Army()
    small_army.add_squads(squadb)
    small_army.add_squads(squadm)
    small_army.add_squads(squadmb)
    actual = str(small_army)
    expected = '''Squad:Brains\nSquad:Monkey\nSquad:Monkey Brains\n'''
    assert actual == expected

def test_is_heavy():
    assert HeavyWeapons

def test_is_sniper():
    assert Sniper

def test_is_machine():
    assert MachineGunner

# @pytest.mark.skip()
def test_add_soldier():
    mark = Sniper("Mark")
    tammy = HeavyWeapons("Tammy")
    ronix = MachineGunner("Ronix")
    squad = Squad("Patchy")
    squad.add_soldiers(mark)
    squad.add_soldiers(tammy)
    squad.add_soldiers(ronix)
    actual = squad.soldiers["Mark"]
    expected = mark
    assert actual == expected

def test_is_soldier_iterable():
    mark = Sniper("Mark")
    tammy = HeavyWeapons("Tammy")
    ronix = MachineGunner("Ronix")
    squad = Squad("Patchy")
    squad.add_soldiers(mark)
    squad.add_soldiers(tammy)
    squad.add_soldiers(ronix)
    actual = ""
    for soldiers in squad:
        actual += f"{soldiers.name} "
    expected = "Mark Tammy Ronix "
    assert actual == expected

def test_is_soldier_health():
    mark = Sniper("Mark")
    tammy = HeavyWeapons("Tammy")
    ronix = MachineGunner("Ronix")
    squad = Squad("Patchy")
    squad.add_soldiers(mark)
    squad.add_soldiers(tammy)
    squad.add_soldiers(ronix)
    actual = 0
    for soldier in squad:
        actual += soldier.health
    expected = 325
    assert actual == expected

def test_soldier_health():
    mark = Sniper("Mark")
    tammy = HeavyWeapons("Tammy")
    ronix = MachineGunner("Ronix")
    squad = Squad("Patchy")
    squad.add_soldiers(mark)
    squad.add_soldiers(tammy)
    squad.add_soldiers(ronix)
    actual = squad.squad_health()
    expected = 325
    assert actual == expected

def test_soldier_names():
    mark = Sniper("Mark")
    tammy = HeavyWeapons("Tammy")
    ronix = MachineGunner("Ronix")
    squad = Squad("Patchy")
    squad.add_soldiers(mark)
    squad.add_soldiers(tammy)
    squad.add_soldiers(ronix)
    actual = str(squad)
    expected = "Patchy with: Mark Tammy Ronix"
    assert actual == expected

def test_str_army():
    mark = Sniper("Mark")
    tammy = HeavyWeapons("Tammy")
    ronix = MachineGunner("Ronix")
    peeps = {mark.name:mark, tammy.name:tammy, ronix.name:ronix}
    squadmb = Squad("Monkey Brains", peeps)
    mark = Sniper("Mar")
    tammy = HeavyWeapons("Tam")
    ronix = MachineGunner("Ron")
    peeps = {mark.name:mark, tammy.name:tammy, ronix.name:ronix}
    squadb = Squad("Brains", peeps)
    mark = Sniper("M")
    tammy = HeavyWeapons("T")
    ronix = MachineGunner("R")
    peeps = {mark.name:mark, tammy.name:tammy, ronix.name:ronix}
    squadm = Squad("Monkey", peeps)
    small_army = Army("Marco's Army")
    small_army.add_squads(squadb)
    small_army.add_squads(squadm)
    small_army.add_squads(squadmb)
    actual = str(small_army)
    expected = '''Marco's Army: Squad:Brains with: Mar Tam Ron\nSquad:Monkey with: M T R\nSquad:Monkey Brains with: Mark Tammy Ronix\n'''
    assert actual == expected

def test_army_is_empty():
    small_army = Army("Test Army")
    actual = str(small_army)
    expected = "Test Army: "
    assert actual == expected

def test_squad_is_empty():
    squad = Squad("Yoda")
    actual = str(squad)
    expected = "Yoda with:"
    assert actual == expected