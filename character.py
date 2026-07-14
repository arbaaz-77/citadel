from house import House


class Character:

    def __init__(self, name, house, title):

        self.name = name
        self.house = house
        self.title = title

    def introduce(self):
        print(
            f"I am {self.name}. \nI belong to House {self.house.name}. \nMy title is {self.title}."
        )

    def to_dict(self):
        return {"name": self.name, "house": self.house, "title": self.title}

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["house"], data["title"])
