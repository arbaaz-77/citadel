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
        return {"name": self.name, "house": self.house.to_dict(), "title": self.title}

    @classmethod
    def from_dict(cls, data, houses):
        house_data = data["house"]
        house_key = house_data["name"].strip().casefold()

        house = houses.get(house_key)

        if house is None:
            house = House.from_dict(house_data)
            houses[house_key] = house

        return cls(data["name"], house, data["title"])
