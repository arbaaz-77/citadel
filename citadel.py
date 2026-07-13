import json

class Character:

    def __init__(self, name, house, title):

        self.name = name
        self.house = house
        self.title = title

    def introduce(self):
        print(f"I am {self.name}. \nI belong to House {self.house}. \nMy title is {self.title}.")

    def to_dict(self):
        return {
            "name": self.name,
            "house": self.house,
            "title": self.title
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["house"],
            data["title"]
        )


class Archive:
    def __init__(self, characters=None):
        self.characters = characters if characters is not None else []

    def view_characters(self):
        if not self.characters:
            print("The archive contains no records.")
            return
        
        for character in self.characters:
            print(f"Name: {character.name}")
            print(f"House: {character.house}")
            print(f"Title: {character.title}")
            print("-" * 35)

    def find_character(self, name):
        for character in self.characters:
            if character.name.casefold() == name.strip().casefold():
                return character

        return None

    def add_character(self, character):
        if not isinstance(character, Character):
            print("Only Character objects can be added.")
            return

        if self.find_character(character.name):
            print(f"{character.name} already exists in the archive.")
            return

        self.characters.append(character)
        print(f"{character.name} added successfully.")
    
    def remove_character(self, name):
        character = self.find_character(name)

        if character:
            self.characters.remove(character)
            print(f"Character {character.name} removed successfully.")
        else:
            print("No record exists.")

    def save(self):
        character_data = []

        for character in self.characters:
            character_data.append(character.to_dict())

        with open("characters.json", "w", encoding="utf-8") as file:
            json.dump(character_data, file, indent=4)

        print("Archive saved successfully.")

    def load(self):
        try:
            with open("characters.json", "r", encoding="utf-8") as file:
                character_data = json.load(file)

            self.characters = []

            for data in character_data:
                character = Character.from_dict(data)
                self.characters.append(character)

            print("Archive loaded successfully.")

        except FileNotFoundError:
            print("No archive found. Starting with the default records.")

        except json.JSONDecodeError:
            print("The archive is damaged. Starting with the default records.")


# functions


def show_menu():
    print("\n===== THE CITADEL ARCHIVE =====")
    print("1. View Characters")
    print("2. Search Character")
    print("3. Add Character")
    print("4. Remove Character")
    print("5. Save Archive")
    print("6. Exit")

def add_character_from_input(archive):
    name = input("Enter character name: ").strip()
    house = input("Enter character house: ").strip()
    title = input("Enter character title: ").strip()

    if not name:
        print("Character name cannot be empty.")
        return
    
    character = Character(name,house,title)
    archive.add_character(character)

def search_character_from_input(archive):
    search_name = input("Enter the name of the character to search: ").strip()
    character = archive.find_character(search_name)
    
    if character:
        print(f"Character found!")
        print(f"Name: {character.name}")
        print(f"House: {character.house}")
        print(f"Title: {character.title}")
    else:
        print("No record exists.")

def remove_character_from_input(archive):
    name = input("Enter name of the character to remove: ").strip()

    archive.remove_character(name)

# Character Data
characters = [
    Character(
        "Jon Snow",
        "Stark",
        "King in the North"
    ),
    Character(
        "Tyrion Lannister",
        "Lannister",
        "Hand of the King"
    ),
    Character(
        "Daenerys Targaryen",
        "Targaryen",
        "Mother of Dragons"
    )
]


# Program runs here
def main():
    archive.load()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == '1':
            archive.view_characters()
        elif choice == '2':
            search_character_from_input(archive)
        elif choice == '3':
            add_character_from_input(archive)
        elif choice == '4':
            remove_character_from_input(archive)
        elif choice == '5':
            archive.save()
        elif choice == '6':
            archive.save()
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")

archive = Archive(characters)
if __name__ == "__main__":
    main()