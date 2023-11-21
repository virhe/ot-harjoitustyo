from entities.character import Character
from entities.player_class import Barbarian
from entities.race import Human

pclass = Barbarian()
prace = Human()

player_character = Character("Example", pclass, prace)

print(player_character)
