from room import Room
from player import Player
from item import Item, Treasure, LightSource

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
room["outside"].populate_item(
    Item(
        "Crimson", "The weapon fills its bearer with an unquenchable thirst for blood."
    )
)
room["outside"].populate_item(
    Item("Tonic", "Seals wounds and mends broken bones for all injuries sustained.")
)
room["foyer"].populate_item(
    Item(
        "Butcher",
        "Embodiment of the madness and depravity that overwhelmed the people of Cairn following the Grim Dawn.",
    )
)
room["overlook"].populate_item(
    Item(
        "Final",
        "Forged by railyard workers during a desparate battle against the rising Chthonian forces.",
    )
)
room["narrow"].populate_item(
    Item(
        "Codex",
        "Forbidden texts of the witch god Solael, as recorded by Cabalist Hester Maughan.",
    )
)
room["treasure"].populate_item(
    Item(
        "Glyph",
        "Signet granted by Kelphat'Zoth, Grand Harbinger of Ch'Thon, upon his most loyal followers.",
    )
)
room["narrow"].populate_item(
    Item(
        "Aegis",
        "The guiding light of Ishtak cleanses of pain and fills with renewed resolve.",
    )
)


# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
