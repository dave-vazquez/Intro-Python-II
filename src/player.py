class Player:
    def __init__(self, name, current_room):
        self.name = name
        current_room = current_room

    def __str__(self):
        return f"{{ name: {self.name}, current_room: {self.current_room} }}"
