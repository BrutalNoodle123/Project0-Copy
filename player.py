class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []

    def pick_up_item(self, item):
        print("You picked up a", item.name)
        self.inventory.append(item)

    def give_item(self, item, character):
        if item in self.inventory:
            character.inventory.append(item)
            self.inventory.remove(item)