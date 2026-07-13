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


jon = Character("Jon Snow", "Stark", "King in the North")
tyrion = Character("Tyrion Lannister", "Lannister", "Hand of the King")
arya = Character("Arya Stark", "Stark", "No One")

archive = Archive([jon, tyrion, arya])

for character in archive.characters:
    character.introduce()