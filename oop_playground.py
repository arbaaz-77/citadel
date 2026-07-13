class Character:

    def __init__(self, name, house, title):

        self.name = name
        self.house = house
        self.title = title

    def introduce(self):
        print(f"I am {self.name}. \nI belong to House {self.house}. \nMy title is {self.title}.")


class Archive:
    def __init__(self, characters=None):
        if characters is None:
            characters = []

        self.characters = characters

    def view_characters(self):
        for character in self.characters:
            character.introduce()


    def add_character(self, character):
        if not isinstance(character, Character):
            print("Only Character objects can be added.")
            return
        
        if self.find_character(character.name):
            print(f"{character.name} already exists in the archive.")
            return
        
        self.characters.append(character)
        print(f"{character.name} added successfully.")

    def find_character(self, name):
        for character in self.characters:
            if character.name.strip().casefold() == name.strip().casefold():
                return character
        return None




jon = Character("Jon Snow", "Stark", "King in the North")
tyrion = Character("Tyrion Lannister", "Lannister", "Hand of the King")
arya = Character("Arya Stark", "Stark", "No One")
brienne = Character("Brienne of Tarth", "Tarth", "Lord Commander of the Kingsguard")

archive = Archive([jon, tyrion, arya])
archive.add_character(brienne)

character = archive.find_character("Jon Snow")

if character:
    character.introduce()
