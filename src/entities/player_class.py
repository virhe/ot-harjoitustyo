"""This module represents the PlayerClass class and its subclasses"""


class PlayerClass:
    """Represents a player class"""

    def __init__(self, name: str, skills: list, class_features: list) -> None:
        """Class constructor"""
        self.name = name
        self.skills = skills
        self.class_features = class_features

    def __str__(self) -> str:
        """Returns PlayerClass as a string, mostly for testing purposes"""
        skill_lines = "\n".join(self.skills)
        class_feature_lines = "\n".join(self.class_features)

        return f"{self.name}:\n{skill_lines}\n{class_feature_lines}\n\n"


# PlayerClass subclasses
class Barbarian(PlayerClass):
    """Represents the barbarian class"""

    def __init__(self) -> None:
        """Class constructor"""
        self.name = "Warrior"
        self.skills = ["Rage", "Unarmored Defense"]
        self.class_features = [
            "Hit Dice: 1d12 per barbarian level",
            "Hit Points at 1st Level: 12 + your Constitution modifier",
            "Hit Points at Higher Levels: 1d12 (or 7) + your Constitution modifier per barbarian "
            "level after 1st",
        ]

        super().__init__(self.name, self.skills, self.class_features)
