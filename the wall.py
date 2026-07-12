def announce_watch():
    print("Night gathers, and now my watch begins.")

announce_watch()
announce_watch()
announce_watch()

def introduce_character(name, house):
    print(f"{name} belongs to {house}.")

introduce_character("Jon Snow", "Stark")

def calculate_dragons(dragon_eggs):
    return dragon_eggs

total = calculate_dragons(5)

def calculate_gold(amount):
    return amount - amount * 0.15

gold = calculate_gold(1000)
print(gold)

# we use return instead of print because we want to use the value later in the program, not just display it.