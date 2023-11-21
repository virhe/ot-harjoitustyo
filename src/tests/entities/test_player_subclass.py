import unittest

from src.entities.player_class import PlayerClass


class TestPlayerClass(unittest.TestCase):
    def test_player_class_can_be_initialized(self):
        player_class = PlayerClass("Testi", list("testi"), list("testi"))
        assert player_class is not None
