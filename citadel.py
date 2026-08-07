from archive import Archive
from character import Character
from house import House


# functions
def show_menu() -> None:
    print("\n===== THE CITADEL ARCHIVE =====")
    print("1. View Characters")
    print("2. Search Character")
    print("3. Add Character")
    print("4. Remove Character")
    print("5. Save Archive")
    print("6. Exit")


def add_character_from_input(archive: Archive, houses: dict[str, House]) -> None:
    name = input("Enter character name: ").strip()
    house_name = input("Enter character house: ").strip().casefold()
    title = input("Enter character title: ").strip()

    if not name:
        print("Character name cannot be empty.")
        return

    house = houses.get(house_name)

    if house is None:
        print("That house does not exist in the archive.")
        return

    character = Character(name, house, title)
    archive.add_character(character)


def search_character_from_input(archive: Archive) -> None:
    search_name = input("Enter the name of the character to search: ").strip()
    character = archive.find_character(search_name)

    if character:
        print("Character found!")
        print(f"Name: {character.name}")
        print(f"House: {character.house.name}")
        print(f"Title: {character.title}")
    else:
        print("No record exists.")


def remove_character_from_input(archive: Archive) -> None:
    name = input("Enter name of the character to remove: ").strip()

    archive.remove_character(name)


# House Data

stark = House("Stark", "Winter is Coming", "Direwolf", "The North")

lannister = House("Lannister", "Hear Me Roar!", "Lion", "The Westerlands")

targaryen = House("Targaryen", "Fire and Blood", "Three-Headed Dragon", "Dragonstone")

houses: dict[str, House] = {
    stark.name.casefold(): stark,
    lannister.name.casefold(): lannister,
    targaryen.name.casefold(): targaryen,
}

# Character Data
characters: list[Character] = [
    Character("Jon Snow", stark, "King in the North"),
    Character("Tyrion Lannister", lannister, "Hand of the King"),
    Character("Daenerys Targaryen", targaryen, "Mother of Dragons"),
]


# Program runs here
def main() -> None:
    archive.load()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            archive.view_characters()
        elif choice == "2":
            search_character_from_input(archive)
        elif choice == "3":
            add_character_from_input(archive, houses)
        elif choice == "4":
            remove_character_from_input(archive)
        elif choice == "5":
            archive.save()
        elif choice == "6":
            archive.save()
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")


archive: Archive = Archive(characters, houses)
if __name__ == "__main__":
    main()
