from PyInquirer import prompt
from colorama import Fore, init
from player import player, InvalidMoveError
from room import rooms
from menus import main_menu, direction_menu, item_menu
import os

cmd = ""
direction = ""
dead_end = False
room_empty = False
inventory_empty = False

# sets colorama autoreset to true
# prevents text color retention
init(autoreset=False)


def print_warning_message():
    global dead_end, room_empty, inventory_empty

    if dead_end:
        print_dead_end()
        dead_end = False
    elif room_empty:

        print_room_empty()
        room_empty = False
    elif inventory_empty:
        print_inventory_empty()
        inventory_empty = False


while not cmd == "Quit":
    # clears terminal
    # TODO: requires detection for os, "clear" works only for mac
    os.system("clear")

    current_room = player.get_current_room()
    room_items = current_room.get_items()
    player_items = player.get_items()

    # displays current room & description
    print(current_room)
    # displays player's inventory
    print(player)
    # displays warning message
    print_warning_message()

    cmd = prompt(main_menu)["menu"]

    if cmd == "Move":
        # prompts user to enter a cardinal direction
        direction = prompt(direction_menu)["direction"]
        try:
            player.move(direction)
        except InvalidMoveError:
            dead_end = True
    elif cmd == "Take Item":
        if current_room.not_empty():
            # initializes item choices to items in room
            item_menu["choices"] = [{"name": item.get_name()} for item in room_items]
            # collects item selections from user
            item_selections = prompt(item_menu)["items"]
            # removes items from current room
            removed_items = current_room.remove_items(item_selections)
            # adds items to player's inventory
            player.add_items(removed_items)
        else:
            room_empty = True

    elif cmd == "Drop Item":
        if player.inventory_not_empty():
            # initializes item choices to items in inventory
            item_menu["choices"] = [{"name": item.get_name()} for item in player_items]
            # collects item selections from user
            item_selections = prompt(item_menu)["items"]
            # removes items from player inventory
            dropped_items = player.drop_items(item_selections)
            # adds items to room
            current_room.add_items(dropped_items)
        else:
            inventory_empty = True

# game end
os.system("clear")
print(Fore.RED + "Your journey has ended. For now...")

