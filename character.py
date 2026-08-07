from typing import Self

from house import House


class Character:

    def __init__(self, name: str, house: House, title: str) -> None:

        self.name = name
        self.house = house
        self.title = title

    def introduce(self) -> None:
        print(
            f"I am {self.name}. \nI belong to House {self.house.name}. \nMy title is {self.title}."
        )

    def to_dict(self) -> dict[str, str | dict[str, str]]:
        return {"name": self.name, "house": self.house.to_dict(), "title": self.title}

    @classmethod
    def from_dict(
        cls, data: dict[str, str | dict[str, str]], houses: dict[str, House]
    ) -> Self:
        house_data = data["house"]
        house_key = house_data["name"].strip().casefold()

        house = houses.get(house_key)

        if house is None:
            house = House.from_dict(house_data)
            houses[house_key] = house

        return cls(data["name"], house, data["title"])
