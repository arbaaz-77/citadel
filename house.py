class House:
    def __init__(self, name, words, sigil, region):
        self.name = name
        self.words = words
        self.sigil = sigil
        self.region = region

    def describe(self):
        print(f"House {self.name}")
        print(f"Words: {self.words}")
        print(f"Sigil: {self.sigil}")
        print(f"Region: {self.region}")

    def to_dict(self):
        return {
            "name": self.name,
            "words": self.words,
            "sigil": self.sigil,
            "region": self.region,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["words"], data["sigil"], data["region"])
