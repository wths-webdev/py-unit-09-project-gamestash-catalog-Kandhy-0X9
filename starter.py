games = {
    "GTA V": 2013,
    "Ratchet & Clank": 2021,
    "Spider-Man: Miles Morales": 2020,
    "God of War Ragnarok": 2022,
    "The Legend of Zelda: Tears of the Kingdom": 2023,
    "Super Mario Odyssey": 2017,
    "Princess Peach": 2024,
    "Mario Kart 8 Deluxe": 2017
}

# get_inventory_count(): Returns how many total games there are in a readable format.
def get_inventory_count():
    print("There are " + str(len(games)) + " games in your inventory.")

# add_game(title, year): Adds a game to the inventory.
def add_game(title, year):
    # update() will add to the dictionary if the key does not exist
    games.update({title: year})

# remove_game(title): Removes a game from the inventory.
def remove_game(game):
    games.pop(game)

# display_inventory()
def display_inventory():
    get_inventory_count()
    # function 2:
    count = 1
    for game in games:
        # for key in games, games[key] returns the value
        print(f"   {str(count)}. {game} by {games[game]}")
        count += 1
    print()

# search_year(year)
def search_year(year):
    year = int(input("Which year would you like to seach for? "))

    print(f"All games from {year}:")
    for game in games:
        if games[game] == year:
            print(f"   {game}")

# search_title(title)
def search_title(title):
    title = input("Which title would you like to search for? ")

    print(f"All games with tittle: {title}:")
    for name in games:
        if name == title:
            print(f" {name}")
#removal
def removal():
    game = input("What title would you like to remove? ")

    remove_game(game)
    print(game + " was removed successfully.")
#adding
def adding():
    print("What game would you like to add?")
    title = input("Title: ")
    year = input("Year released: ")
    add_game(title, year)
#selection
def selection():
    # Display menu to user
    print()
    print("----------- Menu ----------")
    print("Add game (add)")
    print("Remove game (remove)")
    print("Show inventory (show)")
    print("Search by year (year)")
    print("Search for a title (title)")
    print("Quit (q)\n")

# Welcome message
print("\nWelcome to...")
print(" _____________________________  \n"
    "/        _____________        \\\n"
    "| == .  |             |     o |\n"
    "|   _   |             |    B  |\n"
    "|  / \\  |   Game      | A   O |\n"
    "| | O | |      Stash  |  O    |\n"
    "|  \\_/  |             |       |\n"
    "|  :::  |_____________| . . . |\n"
    "\\_____________________________/")

while True:
    selection()
    user_selection = input("What would you like to do? ").lower()

    # Use conditional statements to call functions based on user input
    if user_selection == "add":
        adding()

    elif user_selection == "remove":
        removal()
    
    elif user_selection == "show":
        display_inventory()

    elif user_selection == "year":
        search_year()

    elif user_selection == "title":
        search_title()

    elif user_selection == "q":
        print("Bye bye!")
        break # out of the loop

    else:
        print("Error: That was not an option.\n")

print("")