colors = ["red", "blue", "green", "yellow"]

set1 = [1, 2, 5, 6]
set2 = [3, 4, 7, 8]

fortunes = [
    "You will have a great day!",
    "Something fun is coming soon!",
    "You will learn something cool this week!",
    "A surprise will make you smile!",
    "You will make someone laugh today!",
    "Good luck is headed your way!",
    "You will do something awesome soon!",
    "A happy moment is waiting for you!"
]

# -----------------------------
# FUNCTIONS
# -----------------------------

def display_intro():
    print("✨ Welcome to the Magic Fortune Teller! ✨")
    print()
    print("We are going to play a game just like a paper cootie catcher.")
    print("Follow the steps and your fortune will be revealed!")
    print()
    print("1. First, you will choose a color.")
    print("2. Then, you will choose a number.")
    print("3. Then, you will choose one more number.")
    print("4. Finally... you get your fortune!")
    print()
    print("Let's begin!")
    print("--------------------------------------")


def choose_color():
    return input("Choose a color (red, blue, green, yellow): ")


def choose_number(options):
    print("Choose from:", options)
    return int(input("Number: "))


def flip_numbers(current_set):
    if current_set == set1:
        return set2
    else:
        return set1


def get_starting_set(color):
    if len(color) % 2 == 0:
        return set1
    else:
        return set2


def get_fortune(number):
    return fortunes[number - 1]


# -----------------------------
# MAIN PROGRAM
# -----------------------------

display_intro()

# 1. Choose color
color = choose_color()

# 2. Color affects starting numbers
current_set = get_starting_set(color)

print()
print("Opening based on your color...")
print()

# 3. First number choice
first_choice = choose_number(current_set)

# flip based on first number
for i in range(first_choice):
    current_set = flip_numbers(current_set)

# 4. Second number choice
second_choice = choose_number(current_set)

# 5. Show fortune
print()
print("🔮 Your fortune is:")
print(get_fortune(second_choice))
print("--------------------------------------")