from entities.character import Character
from entities.player_class import *
from entities.race import *

pclass = Barbarian()
prace = Human()

player_character = Character("Example", pclass, prace)

print(player_character)

