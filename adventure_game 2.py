import time
import turtle
import random


def print_pause(sentence):
    print(sentence)
    time.sleep(0)


def intro():
    print_pause("Welcome to our tiny little village")
    print_pause("I suppose that you are here because you heard it.")
    print_pause("Anna, the chief's daugther, is missing!!")
    print_pause("And finally, someone send us you, our hero!!")
    print_pause("Or maybe you are here for the money...")
    print_pause("Anyway, can you help us?")


def play_again(items):
    while True:
        playagain = input("Would you like to play again?"
                          "Say yes or no\n").lower()
        if "yes" in playagain:
            print_pause("Great!!")
            the_village(items)
        elif "no" in playagain:
            print_pause("Ok, bye you boring person.")
            break
        else:
            print_pause("I don't understand troll language.")


def get_help(items):
    response = input("Say yes or no\n").lower()
    if "yes" in response:
        print_pause("Great!!")
        the_village(items)
    elif "no" in response:
        print_pause("Ok, bye...")
    else:
        print_pause("I don't understand troll language.")
        get_help(items)


def sword():
    sword = turtle.Turtle()
    sword.color("green")

    sword.left(60)
    sword.forward(20)
    sword.left(90)
    sword.forward(20)
    sword.right(45)
    sword.forward(10)
    sword.right(90)
    sword.forward(10)
    sword.right(45)
    sword.forward(20)

    sword.left(90)
    sword.forward(100)
    sword.right(45)
    sword.forward(20)
    sword.right(90)
    sword.forward(20)
    sword.right(45)
    sword.forward(100)

    sword.left(90)
    sword.forward(20)
    sword.right(45)
    sword.forward(10)
    sword.right(90)
    sword.forward(10)
    sword.right(45)
    sword.forward(20)

    sword.left(90)
    sword.forward(20)
    sword.right(90)
    sword.forward(30)


def axe():
    axe = turtle.Turtle()
    axe.color("red")

    axe.left(90)
    axe.forward(120)
    axe.left(90)

    for n in range(7):
        axe.left(3)
        axe.forward(10)

    axe.right(100)
    for n in range(10):
        axe.right(3)
        axe.forward(10)

    axe.right(95)
    for n in range(7):
        axe.left(3)
        axe.forward(10)

    axe.forward(30)
    for n in range(7):
        axe.left(3)
        axe.forward(10)

    axe.right(95)
    for n in range(10):
        axe.right(3)
        axe.forward(10)

    axe.right(100)
    for n in range(7):
        axe.left(3)
        axe.forward(10)

    axe.left(95)
    axe.forward(120)
    axe.right(90)
    axe.forward(30)


def grey_house(items):
    if "sword" in items or "axe" in items:
        print_pause("What are you doing in here?")
        print_pause("Go and save Anna!")
    else:
        print_pause("Tell me what you see in the air.")
        weapons = [sword, axe]
        selected_weapon = random.choice(weapons)
        selected_weapon()
        while True:
            arm = input("1. Sword\n"
                        "2. Axe.\n")
            if selected_weapon == sword and arm == "1":
                items.append("sword")
                print_pause("With this, you will win the battle.")
                print_pause("Now, this magic sword is yours.")
                the_village(items)
                break
            elif selected_weapon == axe and arm == "2":
                items.append("axe")
                print_pause("With this, you will win the battle.")
                print_pause("Now, this magic axe is yours.")
                the_village(items)
                break
            else:
                print_pause("You are blind, aren't you?")
                print_pause("I know you can focus, try again.")


def no_invisible_cape(items):
    print_pause("Let's play a game.")
    print_pause("Only if you get a 4 or a 3, I will give something "
                "really special...")
    die_roll = random.randint(1, 6)
    print_pause("*rolling the dice...*")
    print(die_roll)
    if die_roll == 4 or die_roll == 3:
        print_pause("Lucky you, here is my invisible cape.")
        print_pause("Get out of here now.")
        items.append("invisible cape")
        the_village(items)
    else:
        print_pause("ha ha ha, no luck for you today.")
        print_pause("Do you want to try again?")
        dice_answer = input("Yes o no.\n").lower()
        if "yes" in dice_answer:
            shop(items)
        elif "no" in dice_answer:
            the_village(items)
        else:
            print_pause("Are you drunk? I can't understand you.")
            shop(items)


def shop(items):
    if "axe" in items or "sword" in items:
        if "invisible cape" in items:
            print_pause("Are you still alive? Oh, you didn't find Anna yet...")
            the_village(items)
        else:
            no_invisible_cape(items)
    else:
        print_pause("Guess what? We are close for you. Come back "
                    "when you become someone interesting.")
        the_village(items)


def invisible_cape(items):
    print_pause("You have the invisible cape, put it on!!")
    print_pause("He starts saying strange words and "
                "suddenly, everything is dark.")
    print_pause("Thank to the cape, the spell doesn't affect you "
                "and you can see in the darnkness.")
    print_pause("What you are going to do?")
    moment_of_true = input("1.Kill the guy with, "
                           "you don't like him and "
                           "free the girl from the spells thanks to "
                           "your magic weapon.\n"
                           "2.Mehh...you prefer to go "
                           "and have a drink.\n")
    if moment_of_true == "1":
        print_pause("Congratulations!! You win and "
                    "everyone in the village is here to thank you.")
    elif moment_of_true == "2":
        print_pause("Coward.")
    else:
        print_pause("Don't panic, you can talk, what you want to do?")
        tower(items)


def tower(items):
    print_pause("You knock the door and you see the door is open.")
    print_pause("You can see Anna, completely tied in a table.")
    print_pause("And a kind of odd guy praying in some strange language.")
    print_pause("He stops and looks at you with red eyes. Creepy...")
    if "sword" in items or "axe" in items:
        if "invisible cape" in items:
            invisible_cape(items)
        else:
            print_pause("Maybe you need to be more prepared for this.")
            the_village(items)
    else:
        print_pause("No way, you are not ready for this without an arm.")
        the_village(items)


def the_village(items):
    print_pause("In front of you, there are 3 houses.")
    print_pause("Where do you want to go?")
    house = input("1. Grey house\n"
                  "2. Strange empty shop\n"
                  "3. Tiny house with tower\n")
    if house == "1":
        print_pause("Welcome to my humble home.")
        grey_house(items)
    elif house == "2":
        print_pause("Ohhh, you are here to find something else "
                    "to help you rescuing the chief's daughter...")
        shop(items)
    elif house == "3":
        tower(items)
    else:
        print_pause("You don't know how to write... Ok, let's try again.")
        the_village(items)


def adventure_game():
    items = []
    intro()
    get_help(items)
    play_again(items)


adventure_game()
