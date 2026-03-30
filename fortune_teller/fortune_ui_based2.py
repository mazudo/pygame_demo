"""
Fortune Teller UI Example
Uses pygame + pygame_gui

Purpose:
Demonstrate functions, text entry boxes, labels, buttons,
images, and how to turn a text-based program into a UI program.
"""

# -----------------------------
# IMPORTS
# -----------------------------
import pygame
import pygame_gui
import sys
import os


# -----------------------------
# CONSTANTS
# -----------------------------
WIDTH = 700
HEIGHT = 900
FPS = 60
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

COLORS = ["red", "blue", "yellow", "green"]

NUMBERS_SET1 = ["1", "2", "5", "6"]
NUMBERS_SET2 = ["3", "4", "7", "8"]

FORTUNES = {
    "1": "You will have a great day.",
    "2": "A new friend is coming.",
    "3": "You will learn something exciting.",
    "4": "A surprise is in your future.",
    "5": "You will succeed soon.",
    "6": "Good luck is coming your way.",
    "7": "You will make someone smile.",
    "8": "Today will be interesting."
}


# -----------------------------
# GLOBAL VARIABLES
# -----------------------------
current_numbers = NUMBERS_SET1
num_selected_once = False
image = None


# -----------------------------
# FUNCTIONS
# -----------------------------

# Purpose: display a welcome message in the UI
def display_intro():
    title_label.set_text("Magic Fortune Teller")
    instruction_label.set_text(
        "Choose a color, then a number, then one more number to reveal your fortune!"
    )
    status_label.set_text("Type a color to begin.")


# Purpose: load an image file
def load_image(filename):
    try:
        image_path = os.path.join(BASE_DIR, filename)
        return pygame.image.load(image_path)
    except:
        return None


# Purpose: choose the starting number set from the color
def get_number_choices_from_color(color):
    if len(color) % 2 == 0:
        return NUMBERS_SET2
    else:
        return NUMBERS_SET1


# Purpose: choose the next number set from the first number choice
def get_number_choices_from_number(number):
    global current_numbers

    if number % 2 == 1:
        if current_numbers == NUMBERS_SET1:
            return NUMBERS_SET2
        else:
            return NUMBERS_SET1
    else:
        return current_numbers


# Purpose: handle color submission
def submit_color():
    global current_numbers, num_selected_once

    color = color_entry.get_text().lower().strip()

    num_selected_once = False
    current_numbers = get_number_choices_from_color(color)

    color_label.set_text("You chose: " + color.upper())
    number_label.set_text("Pick a number from: " + ", ".join(current_numbers))
    fortune_label.set_text("Your fortune will appear here")
    number_entry.set_text("")
    status_label.set_text("Now choose your first number.")


# Purpose: handle number submission
def submit_number():
    global current_numbers, num_selected_once

    number = number_entry.get_text().strip()

    if number in FORTUNES:
        if num_selected_once:
            fortune = FORTUNES[number]
            fortune_label.set_text("Your fortune: " + fortune)
            status_label.set_text("Fortune revealed!")
        else:
            current_numbers = get_number_choices_from_number(int(number))
            number_label.set_text("Pick ANOTHER number from: " + ", ".join(current_numbers))
            number_entry.set_text("")
            num_selected_once = True
            status_label.set_text("Choose one more number.")


# Purpose: draw the image
def draw_image(surface):
    if image:
        scaled = pygame.transform.scale(image, (320, 320))
        surface.blit(scaled, (190, 500))


# -----------------------------
# MAIN CODE
# -----------------------------
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fortune Teller")

clock = pygame.time.Clock()
manager = pygame_gui.UIManager((WIDTH, HEIGHT))

image = load_image("fortune_teller.png")

# Title
title_label = pygame_gui.elements.UILabel(
    pygame.Rect(180, 20, 340, 30),
    "",
    manager
)

# Instructions
instruction_label = pygame_gui.elements.UILabel(
    pygame.Rect(70, 60, 560, 30),
    "",
    manager
)

# Color input directions
color_prompt_label = pygame_gui.elements.UILabel(
    pygame.Rect(150, 100, 400, 30),
    "Type a color: red, blue, yellow, or green",
    manager
)

# Color input
color_entry = pygame_gui.elements.UITextEntryLine(
    pygame.Rect(265, 140, 170, 35),
    manager
)

color_button = pygame_gui.elements.UIButton(
    pygame.Rect(280, 190, 140, 40),
    "Submit Color",
    manager
)

# Chosen color display
color_label = pygame_gui.elements.UILabel(
    pygame.Rect(180, 250, 340, 30),
    "...",
    manager
)

# Number prompt
number_label = pygame_gui.elements.UILabel(
    pygame.Rect(120, 290, 460, 30),
    "Pick a number from ...",
    manager
)

# Number input
number_entry = pygame_gui.elements.UITextEntryLine(
    pygame.Rect(265, 330, 170, 35),
    manager
)

number_button = pygame_gui.elements.UIButton(
    pygame.Rect(280, 380, 140, 40),
    "Submit Number",
    manager
)

# Fortune label
fortune_label = pygame_gui.elements.UILabel(
    pygame.Rect(70, 440, 560, 40),
    "Your fortune will appear here",
    manager
)

# Status label
status_label = pygame_gui.elements.UILabel(
    pygame.Rect(100, 850, 500, 30),
    "",
    manager
)

display_intro()


# -----------------------------
# GAME LOOP
# -----------------------------
running = True

while running:
    time_delta = clock.tick(FPS) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == color_button:
                submit_color()

            if event.ui_element == number_button:
                submit_number()

        manager.process_events(event)

    manager.update(time_delta)

    screen.fill((84, 72, 72))
    manager.draw_ui(screen)
    draw_image(screen)

    pygame.display.update()

pygame.quit()
sys.exit()