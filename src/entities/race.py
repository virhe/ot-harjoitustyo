"""This module represents the Race class and its subclasses"""


class Race:
    """Represents a player race"""

    def __init__(self, name: str, traits: list) -> None:
        """Class constructor"""
        self.name = name
        self.traits = traits

    def __str__(self) -> str:
        """Returns Race as a string, mostly for testing purposes"""
        trait_lines = "\n".join(self.traits)
        return f"{self.name}:\n{trait_lines}"


# Race subclasses
class Human(Race):
    """Represents the human race"""

    def __init__(self) -> None:
        """Class constructor"""
        self.name = "Human"
        self.traits = ["Ability scores increase: 1"]

        super().__init__(self.name, self.traits)
