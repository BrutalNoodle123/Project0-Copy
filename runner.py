from character import Character
from item import Item
from player import Player
from scene import Scene
from wordle import playWordle

print("Welcome to the game I made last night!")
player_name = input("What is your name?")
player = Player(player_name)
bathroom_vapers = Character("Bathroom Vapers", "A small bandit of law avoiders who contribute to the pollution of greenhouse gases in the bathrooms", [], {"Hello!": "Hey, get out of my stall!", "Instigate": "You do? Great! now get out","Leave": "*They go back to doing weird stuff in the stalls*", "Fight": "Shove nicotine gum inside vapers mouth", "Withdraw": "And stay out!"}, "a nicotine gum")
nicotinegum = Item("nicotine gum", "enhanced gum", 1)
scene1 = Scene("You entered a foggy wasteland at the bottom of the E-building.", bathroom_vapers, nicotinegum)
Skeaton = Character("Mr. Skeaton", "Super mean to me, no reason!", [], {"Hello!": "Shut up Geoff! Why are you such a spazz. I am very busy so go away", "Instigate": "You wanna fight?!!!", "Leave": "*Stares at you all pissed off for no reason*", "Fight": "Use baseball bat and give Skeaton a smack with it", "Withdraw": "Yeah shut up"}, "blank")
baseballbat = Item("baseball bat", "he really want it", 1)
scene2 = Scene("You sense a dark aura", Skeaton, baseballbat)
Edgars = Character("Edgars", "(NBA) No Belt Association", [], {"Hello!": "*Silence*", "Instigate": "You wanna fight fool?", "Leave": "*Goes back to rubbing hair", "Fight": "Use dumbbell to get big muscle and run your 30 real quick", "Withdraw": "Bruh"}, "dumbbells")
dumbbells = Item("dumbbells", "Use this to grow big muscles!", 1)
scene3 = Scene("You go outside of class", Edgars, dumbbells)


choice = 0
while choice != "E":
    print("You are in a econ class. You can either go to the E-Building bathroom, leave class, or stay in class like a good boy! ")
    choice = input("Choose one of the following:\nB - go to the bathroom\nL - leave class\nS - stay in class\nE - exit game\n")
    if choice == "B":
        print("You go to the bathroom, a mysterious and raspy voice asks you for the super duper secret password.")
        win = playWordle("SMOKE")
        if win == True:
            print("You have been granted super confidential access and may enter the bathroom.")
            scene1.enter(player)
    elif choice == "L":
        print("To leave the classroom, you must solve todays word puzzle.")
        win = playWordle("LEAVE")
        if win == True:
            print("Get out of my class loser.")
            scene3.enter(player)
    elif choice == "S":
        print("You stay in class, Skeaton gives a pop quiz.")
        win = playWordle("BALLS")
        if win == True:
            print("Good job... not!")
            scene2.enter(player)
        else:
            print("You failed the word puzzle.")
    else:
        print("Invalid choice. Please enter B, L, S, or E.")

print("Thanks for playing!")