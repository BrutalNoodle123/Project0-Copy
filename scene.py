class Scene:
    def __init__(self, description, character, item):
        self.description = description
        self.character = character
        self.item = item


    def enter(self, player):
        print(self.description)
        print("You see a", self.character.description)
        print("You see a", self.item.name)
        choice = input("Do you want to move toward the characters or the item or leave the scene? (C/I/L): ")
        if choice == "C":
            while choice != "L":
                choice = input("Do you want to talk or leave? (G/L): ")
                if choice == "G":
                    print("You said: Hello!")
                    self.character.talk_to_player("Hello!")
                    choice = input("Analyze what the character needs (Y/N)")
                    if choice == "Y":
                        self.character.ask_for_item()
                        choice = input(f"Do you have what {self.character.name} needs? (Y/N)")
                        if choice == "Y":
                            print("You said: You gonna get it")
                            self.character.talk_to_player("Instigate")
                            choice = input("Do you want to use your item on the character? (Y/N)")
                            if choice == "Y":
                                player.give_item(self.item, self.character)
                                print("You said: Here you go!")
                                self.character.talk_to_player("Fight")
                            else:
                                print("You said: Later Nerds!")
                                self.character.talk_to_player("Withdraw")
                        else:
                            print("You said: Later Nerds!")
                            self.character.talk_to_player("Withdraw")
                    elif choice == "N":
                        print("You said: Later Nerds!")
                        self.character.talk_to_player("Withdraw")
                elif choice == "L":
                    print("You leave the room.")
                    self.enter(player)
                else:
                    print("Invalid choice. Please try again.")
        elif choice == "I":
            choice = input("Do you want to pick it up or examine it? P/E")
            if choice == "P":
                print("You picked up a ", self.item.name)
                player.pick_up_item(self.item)
                self.enter(player)
            elif choice == "E":
                print(f"You found a {self.item.name} {self.item.description}")
                choice = input("Do you want to pick it up now? Y/N")
                if choice == "Y":
                    print("You picked up a ", self.item.name)
                    player.pick_up_item(self.item)
                    self.enter(player)
                else:
                    print("You leave the item.")
                    self.enter(player)
        elif choice == "L":
            print("You leave the room.")
        else:
            print("Invalid choice. Please try again.")
            self.enter(player)