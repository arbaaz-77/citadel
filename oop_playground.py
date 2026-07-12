class Character:

    def __init__(self, name, house, title):

        self.name = name
        self.house = house
        self.title = title

jon = Character("Jon Snow", "Stark", "King in the North")
tyrion = Character("Tyrion Lannister", "Lannister", "Hand of the King")
arya = Character("Arya Stark", "Stark", "Tywin Lannister's cupbearer")

print(f"{jon.name} \nHouse: {jon.house} \nTitle: {jon.title}")
print(f"{tyrion.name} \nHouse: {tyrion.house} \nTitle: {tyrion.title}")
print(f"{arya.name} \nHouse: {arya.house} \nTitle: {arya.title}")