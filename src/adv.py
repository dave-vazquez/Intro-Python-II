from PyInquirer import prompt
from colorama import Fore
from room import rooms
from player import player
import copy
import sys
import os

# function to clear terminal after each input command
def clear():
    return os.system("clear")


clear()

"""
    Main

    Make a new player object that is currently in the 'outside' room.

    Write a loop that:

    * Prints the current room name
    * Prints the current description (the textwrap module might be useful here).
    * Waits for user input and decides what to do.

    # Print an error message if the movement isn't allowed.
    If the user enters a cardinal direction, attempt to move to the room there.

    If the user enters "q", quit the game.
"""

cardinal_directions = [
    {
        "type": "list",
        "name": "menu",
        "message": "What direction do you want to move in?",
        "choices": ["North", "South", "East", "West", "Quit"],
    }
]


cmd = ""
while not cmd == "Quit":
    print(
        Fore.CYAN
        + f"Current Room: {player.current_room.name} \
        \n{player.current_room.description}"
    )

    cmd = prompt(cardinal_directions)["menu"]

    if cmd == "North":
        clear()
        print("Moves North")
    elif cmd == "South":
        clear()
        print("Moves South")
    elif cmd == "East":
        clear()
        print("Moves East")
    elif cmd == "West":
        clear()
        print("Moves West")
    else:
        clear()
        print("Invalid command. Try again.")
clear()
print("Your journey has ended. For now...")

