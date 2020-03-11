from PyInquirer import prompt
from colorama import Fore
from colorama import init
from room import rooms
from player import player
import os

# sets colorama autoreset to true
# prevents text color retention
init(autoreset=False)

# TODO: consider textwrap module
def print_current_room(current_room):
    print(Fore.CYAN + "Current Room: " + Fore.MAGENTA + f"{current_room.name}\n")
    print(Fore.GREEN + f"{current_room.description}\n")


def print_dead_end():
    print(Fore.RED + "You've hit a dead end.\n")


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
    os.system("clear")  # TODO: requires detection for os, "clear" works only for mac

    current_room = player.get_current_room()
    # displays current room & description
    print_current_room(current_room)

    if dead_end is True:
        print_dead_end()
        dead_end = False

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


os.system("clear")
print(Fore.RED + "Your journey has ended. For now...")

