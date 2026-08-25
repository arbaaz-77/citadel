from dataclasses import dataclass
from typing import Self


@dataclass(frozen=True)
class House:
    name: str
    words: str
    sigil: str
    region: str

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
    def from_dict(cls, data: dict[str, str]) -> Self:
        return cls(data["name"], data["words"], data["sigil"], data["region"])
