import json

characters = [
    {
        "name": "Jon Snow",
        "house": "Stark",
        "title": "King in the North"
    },
    {
        "name": "Tyrion Lannister",
        "house": "Lannister",
        "title": "Hand of the King"
    },
    {
        "name": "Daenerys Targaryen",
        "house": "Targaryen",
        "title": "Mother of Dragons"
    }
]

# functions

def show_menu():
    print("\n===== THE CITADEL ARCHIVE =====")
    print("1. View Characters")
    print("2. Search Character")
    print("3. Add Character")
    print("4. Remove Character")
    print("5. Save Archive")
    print("6. Exit")


def view_characters():
    for character in characters:
        print(f"Name: {character['name']}")
        print(f"House: {character['house']}")
        print(f"Title: {character['title']}")
        print("-" * 35)

def search_character():
    search_name = input("Enter the name of the character to search: ").strip()
    character = find_character(search_name)
    
    if character:
        print(f"Character found!")
        print(f"Name: {character['name']}")
        print(f"House: {character['house']}")
        print(f"Title: {character['title']}")
    else:
        print("No record exists.")

def add_character():
    name = input("Enter character name: ").strip()
    house = input("Enter character house: ").strip()
    title = input("Enter character title: ").strip()

    if not name:
        print("Character name cannot be empty.")
        return
    
    if find_character(name):
        print("A character with that name already exists.")
        return

    characters.append({"name": name, "house": house, "title": title})
    print(f"Character {name} added successfully.")

    

def remove_character():
    name = input("Enter the name of the character to remove: ").strip()
    character = find_character(name)

    if character:
        characters.remove(character)
        print(f"Character {character['name']} removed successfully.")
    else:
        print("No record exists.")

def find_character(name):
    for character in characters:
        if character['name'].strip().casefold() == name.strip().casefold():
            return character
    return None

def save_archive():
    with open('characters.json', 'w', encoding="utf-8") as file:
        json.dump(characters, file, indent=4)
    print("Archive saved successfully.")

def load_archive():
    global characters

    try:
        with open("characters.json", "r") as file:
            characters = json.load(file)

        print("Archive loaded successfully.")

    except FileNotFoundError:
        print("No archive found. Starting with the default records.")

    except json.JSONDecodeError:
        print("The archive is damaged. Starting with the default records.")



# Program runs here


load_archive()

while True:
    show_menu()
    choice = input("Choose an option: ").strip()
    if choice == '1':
        view_characters()
    elif choice == '2':
        search_character()
    elif choice == '3':
        add_character()
    elif choice == '4':
        remove_character()
    elif choice == '5':
        save_archive()
    elif choice == '6':
        save_archive()
        print("Goodbye.")
        break
    else:
        print("Invalid choice. Please try again.")