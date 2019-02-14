# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, desc, is_lit=False):
        self.name = name
        self.desc = desc
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = []
        self.is_lit = is_lit

    def populate_item(self, item):
        self.items.append(item)