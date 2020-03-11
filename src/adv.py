from PyInquirer import prompt
from colorama import Fore
from room import rooms
from player import player
import copy
import sys
import os

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


def print_current_room(player):
    print(
        Fore.CYAN
        + f"Current Room: {player.current_room.name} \
        \n\n{player.current_room.description}\n"
    )


cardinal_directions = [
    {
        "type": "list",
        "name": "menu",
        "message": "What direction do you want to move in?",
        "choices": ["North", "South", "East", "West", "Quit"],
    }
]

cmd = ""
dead_end = False

while not cmd == "Quit":
    # clears terminal
    os.system("clear")  # mac os

    if dead_end is True:
        print(Fore.RED + "You've hit a dead end.\n")
        dead_end = False

    # displays current room & description
    print_current_room(player)

    # prompts user to enter a cardinal direction
    cmd = prompt(cardinal_directions)["menu"]
    try:
        if cmd == "North":
            player.move(cmd)
        elif cmd == "South":
            player.move(cmd)
        elif cmd == "East":
            player.move(cmd)
        elif cmd == "West":
            player.move(cmd)
    except AttributeError:
        dead_end = True


clear()
print("Your journey has ended. For now...")

