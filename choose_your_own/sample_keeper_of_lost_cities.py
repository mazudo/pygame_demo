############################################################
# Magical Adventure – Inspired by Keeper of the Lost Cities
#
# In this story, you discover that you have special abilities
# and are invited to explore the hidden elvin world.
#
# Your choices will change what happens!
############################################################


print("Welcome to the Hidden Cities Adventure!")
print("You are walking home from school when something strange happens.")
print("You suddenly hear someone speaking... but no one is nearby.")


############################################################
# First Decision
############################################################

choice1 = input(
    "\nA mysterious boy appears and says he can hear your thoughts.\n"
    "Do you:\n"
    "A) Ask him how he did that\n"
    "B) Run away\n"
    "Type A or B: "
).lower()


if choice1 == "a":

    print("\nThe boy smiles.")
    print('"You are a telepath," he says. "And you belong in the Lost Cities."')

    ############################################################
    # Second Decision
    ############################################################

    choice2 = input(
        "\nHe offers to take you through a magical portal.\n"
        "Do you:\n"
        "A) Go through the portal\n"
        "B) Ask more questions first\n"
        "Type A or B: "
    ).lower()

    if choice2 == "a":

        print("\nYou step through the portal and arrive in a beautiful glowing city!")
        print("Tall crystal towers shine in the sunlight.")

        ############################################################
        # Third Decision
        ############################################################

        choice3 = input(
            "\nAt the academy, you must choose your first class.\n"
            "Do you choose:\n"
            "A) Telepathy training\n"
            "B) Creature studies\n"
            "Type A or B: "
        ).lower()

        if choice3 == "a":
            print("\nYour telepathy is incredibly strong!")
            print("The teachers think you may become one of the greatest telepaths ever.")

        elif choice3 == "b":
            print("\nYou meet a baby alicorn in the creature sanctuary!")
            print("It seems to trust you immediately.")

        else:
            print("\nThe teachers are confused by your answer and send you to orientation.")

    elif choice2 == "b":

        print("\nYou ask many questions about the Lost Cities.")
        print("The boy explains that elves have hidden from humans for centuries.")

        choice3 = input(
            "\nDo you:\n"
            "A) Trust him and go through the portal\n"
            "B) Decide to stay in the human world\n"
            "Type A or B: "
        ).lower()

        if choice3 == "a":
            print("\nYou bravely step through the portal and begin your new life in the Lost Cities!")

        elif choice3 == "b":
            print("\nYou decide you are not ready yet.")
            print("But the boy says he will return when you are ready.")

        else:
            print("\nThe portal flickers and disappears while you hesitate.")

    else:
        print("\nThe boy waits patiently, unsure what you want to do.")


elif choice1 == "b":

    print("\nYou run down the street as fast as you can.")
    print("But the mysterious boy easily catches up.")

    choice2 = input(
        "\nHe says, 'Running won't help. You have powers.'\n"
        "Do you:\n"
        "A) Listen to him\n"
        "B) Keep running\n"
        "Type A or B: "
    ).lower()

    if choice2 == "a":
        print("\nYou stop and listen.")
        print("Soon you learn about the hidden elvin world and your place in it.")

    elif choice2 == "b":
        print("\nYou keep running until the strange voice disappears.")
        print("But later that night... you hear thoughts again.")

    else:
        print("\nYou freeze in confusion while the mysterious boy sighs.")


else:
    print("\nYou stand silently, unsure what to do.")


############################################################
# Ending
############################################################

print("\nThe adventure ends... for now.")
print("Try running the program again and make different choices!")