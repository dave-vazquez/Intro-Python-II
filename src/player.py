from room import rooms


class Player:
    def __init__(self, name, current_room, items=None):
        self.name = name
        self.current_room = current_room
        self.items = items

    def get_current_room(self):
        return self.current_room

    def get_items(self):
        return self.items

    def move(self, direction):
        if direction == "North":
            self.current_room = self.current_room.n_to
        elif direction == "South":
            self.current_room = self.current_room.s_to
        elif direction == "East":
            self.current_room = self.current_room.e_to
        elif direction == "West":
            self.current_room = self.current_room.e_to

    def __str__(self):
        return f"{{ name: {self.name}, current_room: {self.current_room} }}"


player = Player("hero", rooms["outside"])
