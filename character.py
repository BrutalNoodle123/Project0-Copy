class Character:
    def __init__(self, name, description, inventory, dialogue, looking_for):
        self.name = name
        self.description = description
        self.inventory = inventory
        self.dialogue = dialogue
        self.looking_for = looking_for

    def talk_to_player(self, player_msg):
        for sentence in self.dialogue:
            if player_msg == sentence:
                print(self.name, "said", self.dialogue[sentence])

    def ask_for_item(self):
        print("This character needs to get smacked by " + self.looking_for)

    def receive_item(self, item):
        self.inventory.append(item)