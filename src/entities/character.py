from src.entities.player_class import PlayerClass
from src.entities.race import Race


class Character:
    def __init__(self, name: str, player_class: PlayerClass, race: Race) -> None:
        self.name = name
        self.player_class = player_class
        self.race = race

    def __str__(self) -> str:
        character_description = f"{self.name} | {self.player_class.name} | {self.race.name}\n\n"

        return character_description + str(self.player_class) + str(self.race)
