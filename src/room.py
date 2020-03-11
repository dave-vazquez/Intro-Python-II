class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return f" {{ name: {self.name}, description: {self.description} }}"


# declare all the rooms
rooms = {
    "outside": Room("Outside Cave Entrance", "North of you, the cave mount beckons..."),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east...""",
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm...""",
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air...""",
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
