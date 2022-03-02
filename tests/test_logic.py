import pytest
from tests.flo import diff
from pythonisms.battle_logic import Game


def test_is_game():
  assert Game

def test_test():
  expected = 4
  actual = 1 + 3
  assert expected == actual

def test_start_game():
  diffs = diff(Game().start_game, path="tests/sim/start.sim.txt")
  assert not diffs, diffs

# @pytest.mark.skip()
def test_play_game():
  diffs = diff(Game().start_game, path="tests/sim/play.sim.txt")
  assert not diffs, diffs

def test_shop_game():
  diffs = diff(Game().start_game, path="tests/sim/shop.sim.txt")
  assert not diffs, diffs

def test_shop_leave_game():
  diffs = diff(Game().start_game, path="tests/sim/shop_leave.sim.txt")
  assert not diffs, diffs

def test_shop_train_game():
  diffs = diff(Game().start_game, path="tests/sim/shop_train.sim.txt")
  assert not diffs, diffs
