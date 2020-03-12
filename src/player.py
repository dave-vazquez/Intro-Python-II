from item import Item
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
        if direction == "North" and self.current_room.n_to is not None:
            self.current_room = self.current_room.n_to
        elif direction == "South" and self.current_room.s_to is not None:
            self.current_room = self.current_room.s_to
        elif direction == "East" and self.current_room.e_to is not None:
            self.current_room = self.current_room.e_to
        elif direction == "West" and self.current_room.w_to is not None:
            self.current_room = self.current_room.w_to
        else:
            raise InvalidMoveError()

    def __str__(self):
        return f"{{ name: {self.name}, current_room: {self.current_room} }}"


class InvalidMoveError(Exception):
    pass


player = Player("hero", rooms["outside"])
