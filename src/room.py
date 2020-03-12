from item import Item
import copy


class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_items(self):
        return self.items

    def add_items(self, items):
        self.items.extend(items)

    def remove_items(self, item_names):
        removed_items = []

        indices_to_remove = [
            idx for idx, item in enumerate(self.items) if item.get_name() in item_names
        ]

        for idx in indices_to_remove:
            removed_items.append(self.items[idx])

        self.items = [
            item for idx, item in enumerate(self.items) if idx not in indices_to_remove
        ]

        return removed_items

    def not_empty(self):
        return len(self.items) > 0

    def __str__(self):
        return f" {{ name: {self.name}, description: {self.description} }}"


# declare all the rooms
rooms = {
    "outside": Room(
        "Outside Cave Entrance",
        "North of you, the cave mount beckons...",
        [
            Item("Rock", "A large stone made from basalt."),
            Item("Paper", "A sheet of paper made of papyrus."),
            Item("Scissors", "A marvelous new piece of technology."),
        ],
    ),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east...""",
        [
            Item("Gold", "A few peices of gold."),
            Item("Helmet", "Something to protect your head.."),
            Item("Shield", "Something to protect your body."),
        ],
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm...""",
        [
            Item("Skull", "A previous traveler's skull."),
            Item("Hide", "Hide from a Cow."),
            Item("Bow", "An old bow."),
        ],
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air...""",
        [
            Item("Sword", "A large iron sword."),
            Item(
                "Arrow",
                "This one looks as if it had been lodged into the knee of an adventurer...",
            ),
            Item("Leather Pants", "Chapped, ass-less, leather pants."),
        ],
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south...""",
    ),
}

# link rooms together
rooms["outside"].n_to = rooms["foyer"]
rooms["foyer"].s_to = rooms["outside"]
rooms["foyer"].n_to = rooms["overlook"]
rooms["foyer"].e_to = rooms["narrow"]
rooms["overlook"].s_to = rooms["foyer"]
rooms["narrow"].w_to = rooms["foyer"]
rooms["narrow"].n_to = rooms["treasure"]
rooms["treasure"].s_to = rooms["narrow"]
