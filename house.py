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
