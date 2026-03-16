"""
Author: Example for Fortune Teller Assignment
Purpose: A simple paper fortune teller program that demonstrates
         functions, parameters, arguments, user input, and choices.

Program flow:
1. User chooses one of 4 colors.
2. The program "counts" by the number of letters in that color.
3. User chooses one of the visible numbers.
4. The program counts again.
5. User chooses a final number.
6. The program displays a fortune.
"""

# -----------------------------
# IMPORTS
# -----------------------------

# No imports needed for this program.


# -----------------------------
# CONSTANTS
# -----------------------------

COLORS = ["red", "blue", "green", "yellow"]

# After an odd number of moves, these numbers are visible.
ODD_NUMBERS = [1, 2, 5, 6]

# After an even number of moves, these numbers are visible.
EVEN_NUMBERS = [3, 4, 7, 8]

FORTUNES = [
    "You will have a great day.",
    "A new opportunity is coming soon.",
    "You will learn something exciting this week.",
    "Good luck is headed your way.",
    "You will make someone smile today.",
    "A fun surprise is in your future.",
    "You will succeed if you keep trying.",
    "Something positive will happen soon."
]


# -----------------------------
# FUNCTIONS
# -----------------------------

# Purpose: Displays a welcome message and explains how the program works.
# Input: None
# Output: None
def display_intro():
    print("Welcome to the Paper Fortune Teller!")
    print("First, choose a color.")
    print("Then choose a number.")
    print("Then choose one more number to reveal your fortune.")
    print()


# Purpose: Shows the list of available colors to the user.
# Input: None
# Output: None
def display_colors():
    print("Available colors:")
    for color in COLORS:
        print("-", color)
    print()


# Purpose: Gets a valid color choice from the user.
# Input: None
# Output: Returns the user's chosen color as a string
def get_color_choice():
    user_color = input("Choose a color: ").lower()

    # Keep asking until the user enters a valid color.
    while user_color not in COLORS:
        print("That is not a valid color.")
        user_color = input("Choose red, blue, green, or yellow: ").lower()

    return user_color


# Purpose: Counts how many times the fortune teller should move
#          based on the length of the chosen color.
# Input: color_choice - a string containing the user's chosen color
# Output: Returns the number of letters in the color as an integer
def count_color_letters(color_choice):
    return len(color_choice)


# Purpose: Determines which numbers should be shown after a move count.
# Input: move_count - an integer representing how many times the teller moved
# Output: Returns a list of visible numbers
def get_visible_numbers(move_count):
    # Odd counts show one set of numbers.
    if move_count % 2 == 1:
        return ODD_NUMBERS
    else:
        return EVEN_NUMBERS


# Purpose: Displays the currently visible numbers.
# Input: visible_numbers - a list of integers
# Output: None
def display_numbers(visible_numbers):
    print("Available numbers:")
    for number in visible_numbers:
        print("-", number)
    print()


# Purpose: Gets a valid number choice from the user from the visible numbers.
# Input: visible_numbers - a list of integers the user may choose from
# Output: Returns the chosen number as an integer
def get_number_choice(visible_numbers):
    user_number = int(input("Choose one of those numbers: "))

    # Keep asking until the user enters one of the visible numbers.
    while user_number not in visible_numbers:
        print("That number is not available right now.")
        user_number = int(input("Choose one of the visible numbers: "))

    return user_number


# Purpose: Looks up the fortune that matches the final chosen number.
# Input: final_number - an integer from 1 to 8
# Output: Returns the matching fortune as a string
def get_fortune(final_number):
    return FORTUNES[final_number - 1] # subtract one since list starts from zero index


# Purpose: Displays the final fortune to the user.
# Input: fortune_text - a string containing the fortune
# Output: None
def display_fortune(fortune_text):
    print()
    print("Your fortune is:")
    print(fortune_text)
    print("##############################################")
    print()


# -----------------------------
# MAIN CODE
# -----------------------------
# implement the following functions
# some are basic
# some accept parameters
# some accept parameters and return values

display_intro()

# First choice: color
display_colors()
chosen_color = get_color_choice()

# Move based on number of letters in the chosen color
first_move_count = count_color_letters(chosen_color)
# numbers that fortune teller shows to the player
first_visible_numbers = get_visible_numbers(first_move_count)

# Second choice: first number
display_numbers(first_visible_numbers)
# user's first number choice from prompt
first_number_choice = get_number_choice(first_visible_numbers)

# Move again based on the chosen number
second_visible_numbers = get_visible_numbers(first_number_choice)

# Third choice: final number
display_numbers(second_visible_numbers)
final_number_choice = get_number_choice(second_visible_numbers)

# Show the fortune
fortune = get_fortune(final_number_choice)
display_fortune(fortune)