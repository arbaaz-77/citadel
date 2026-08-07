class House:
    def __init__(self, name: str, words: str, sigil: str, region: str) -> None:
        self.name = name
        self.words = words
        self.sigil = sigil
        self.region = region

    def describe(self) -> None:
        print(f"House {self.name}")
        print(f"Words: {self.words}")
        print(f"Sigil: {self.sigil}")
        print(f"Region: {self.region}")

    def to_dict(self) -> dict[str, str]:
        return {
            "name": self.name,
            "words": self.words,
            "sigil": self.sigil,
            "region": self.region,
        }

    @classmethod
    def from_dict(cls, data: dict[str, str]) -> "House":
        return cls(data["name"], data["words"], data["sigil"], data["region"])
