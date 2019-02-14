# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current, score=0):
        self.name = name
        self.current = current
        self.score = score
        self.inventory = []
    def move_to(self, room):
        if room:
            self.current = self.current.to_new(room)
        else:
            print("You can't go that way.")