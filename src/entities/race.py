# Main race
class Race:
    def __init__(self, name: str, traits: list) -> None:
        self.name = name
        self.traits = traits

    def __str__(self) -> str:
        trait_lines = "\n".join(self.traits)
        return f"{self.name}:\n{trait_lines}"

# Subraces
class Human(Race):
    def __init__(self) -> None:
        self.name = "Human"
        self.traits = ["Ability scores increase: 1"]

        super().__init__(self.name, self.traits)
