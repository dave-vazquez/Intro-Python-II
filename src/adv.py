from PyInquirer import prompt
from colorama import Fore
from colorama import init
from room import rooms
from player import player
from player import InvalidMoveError
import os

# sets colorama autoreset to true
# prevents text color retention
init(autoreset=False)

main_menu = {
    "type": "list",
    "name": "menu",
    "message": "What action would you like to take?",
    "choices": ["Move", "Take Item", "Quit"],
}


direction_menu = (
    {
        "type": "list",
        "name": "direction",
        "message": "Which direction?",
        "choices": ["North", "South", "East", "West", "Back to Menu"],
    },
)


item_menu = {"type": "checkbox", "name": "items", "message": "Select an item"}

# TODO: consider textwrap module
def print_current_room(current_room):
    print(Fore.CYAN + "Current Room: " + Fore.MAGENTA + f"{current_room.name}\n")
    print(Fore.GREEN + f"{current_room.description}\n")


def print_room_items(current_room):
    print(Fore.CYAN + "Items in Room:")
    for item in current_room.get_items():
        print(Fore.MAGENTA + f"{item}")
    print()  # line break

def print_player_items(player):
    print(Fore.CYAN + "Held Items:")
    for item in player.get_items():
        print(Fore.MAGENTA + f"{item}")
    print()  # line break


def print_dead_end():
    print(Fore.RED + "You've hit a dead end.\n")


cmd = ""
direction = ""
dead_end = False

while not cmd == "Quit":
    # clears terminal
    os.system("clear")  # TODO: requires detection for os, "clear" works only for mac

    current_room = player.get_current_room()
    room_items = current_room.get_items()

    # displays current room & description
    print_current_room(current_room)
    # displays items in room
    print_room_items(current_room)
    # displays items held by player
    print_player_items(player)

    if dead_end is True:
        print_dead_end()
        dead_end = False

    cmd = prompt(main_menu)["menu"]

    if cmd == "Move":
        # prompts user to enter a cardinal direction
        direction = prompt(direction_menu)["direction"]
        try:
            player.move(direction)
        except InvalidMoveError:
            dead_end = True
    elif cmd == "Take Item":
        # initializes item choices from items in room
        item_menu["choices"] = [{"name": item.get_name()} for item in room_items]
        # collects item selections from user
        item_selections = prompt(item_menu)["items"]
        # removes items from current room and stores them in removed_items
        removed_items = current_room.remove_items(item_selections)
        # adds items to player's inventory
        player.add_items(removed_items)

# game end
os.system("clear")
print(Fore.RED + "Your journey has ended. For now...")

