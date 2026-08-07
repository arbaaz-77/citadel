import json

from character import Character
from house import House


class Archive:
    def __init__(
        self,
        characters: list[Character] | None = None,
        houses: dict[str, House] | None = None,
    ) -> None:
        self.characters: list[Character] = characters if characters is not None else []
        self.houses: dict[str, House] = houses if houses is not None else {}

    def view_characters(self) -> None:
        if not self.characters:
            print("The archive contains no records.")
            return

        for character in self.characters:
            print(f"Name: {character.name}")
            print(f"House: {character.house.name}")
            print(f"Title: {character.title}")
            print("-" * 35)

    def find_character(self, name: str) -> Character | None:
        for character in self.characters:
            if character.name.casefold() == name.strip().casefold():
                return character

        return None

    def add_character(self, character: Character) -> None:
        if not isinstance(character, Character):
            print("Only Character objects can be added.")
            return

        if self.find_character(character.name):
            print(f"{character.name} already exists in the archive.")
            return

        self.characters.append(character)
        print(f"{character.name} added successfully.")

    def remove_character(self, name: str) -> None:
        character = self.find_character(name)

        if character:
            self.characters.remove(character)
            print(f"Character {character.name} removed successfully.")
        else:
            print("No record exists.")

    def save(self) -> None:
        character_data = []

        for character in self.characters:
            character_data.append(character.to_dict())

        with open("characters.json", "w", encoding="utf-8") as file:
            json.dump(character_data, file, indent=4)

        print("Archive saved successfully.")

    def load(self) -> None:
        try:
            with open("characters.json", "r", encoding="utf-8") as file:
                character_data = json.load(file)

            self.characters = []

            for data in character_data:
                character = Character.from_dict(data, self.houses)
                self.characters.append(character)

            print("Archive loaded successfully.")

        except FileNotFoundError:
            print("No archive found. Starting with the default records.")

        except json.JSONDecodeError:
            print("The archive is damaged. Starting with the default records.")
