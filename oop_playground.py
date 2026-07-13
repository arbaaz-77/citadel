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
        self.characters.append(character)



jon = Character("Jon Snow", "Stark", "King in the North")
tyrion = Character("Tyrion Lannister", "Lannister", "Hand of the King")
arya = Character("Arya Stark", "Stark", "No One")
brienne = Character("Brienne of Tarth", "Tarth", "Lord Commander of the Kingsguard")

archive = Archive([jon, tyrion, arya])
archive.add_character(brienne)

