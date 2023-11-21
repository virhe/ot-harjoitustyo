from .player_class import PlayerClass
from .race import Race


class Character:
    """Represents a player character"""

    def __init__(self, name: str, player_class: PlayerClass, race: Race) -> None:
        """Class constructor"""
        self.name = name
        self.player_class = player_class
        self.race = race

    def __str__(self) -> str:
        """Returns Character as a string, mostly for testing purposes"""
        character_description = (
            f"{self.name} | {self.player_class.name} | {self.race.name}\n\n"
        )

        return character_description + str(self.player_class) + str(self.race)
