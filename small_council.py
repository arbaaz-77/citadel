characters = ["Tyrion", "Davos", "Brienne", "Samwell", "Bran"]
for character in characters:
    print(f"Lord {character} attends the Small Council")

tyrion = {
    "Name": "Tyrion Lannister",
    "Title": "Hand of the King",
    "House": "House Lannister",
    "Weapon": "Wit and Cunning", 
}

for key, value in tyrion.items():
    print(f"{key}: {value}")

dragons = ["Drogon", "Rhaegal", "Viserion"]
chosen_dragon = input("Choose a dragon: ")
if chosen_dragon in dragons:
    print(f"A dragon answers your call!")
else:
    print(f"That dragon does not exist in this realm.")