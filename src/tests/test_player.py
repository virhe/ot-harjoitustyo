
from src.classes.player import Player

def test_player_init():
    player = Player()
    assert player.rect.x == 50
    assert player.rect.y == 50
    assert player.rect.width == 100
    assert player.rect.height == 100