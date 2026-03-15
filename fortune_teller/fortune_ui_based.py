"""
Fortune Teller UI Example
Uses pygame + pygame_gui

Purpose:
Demonstrate functions, buttons, entry boxes, labels, and images.
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
color_length = 0
current_numbers = []
num_selected_once = False
image = None


# -----------------------------
# FUNCTIONS
# -----------------------------

# Purpose: load the fortune teller image
def load_image():
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(base_dir, "fortune_teller.png")
        return pygame.image.load(image_path)
    except:
        return None


# Purpose: determine which numbers to show color length
def get_number_choices(length):
    if length % 2 == 0:
        return NUMBERS_SET2
    else:
        return NUMBERS_SET1
    
# Purpose: determine which numbers to show from number choice
def get_number_choices_from_number(number):
    if number % 2 == 1: # switch only if it odd, else remains the same
        if current_numbers == NUMBERS_SET1:
            return NUMBERS_SET2
        else:
            return NUMBERS_SET1
    else:
        return current_numbers


# Purpose: handle color button press
def submit_color():

    global color_length
    global current_numbers

    color = color_entry.get_text().lower()

    if color in COLORS:

        color_length = len(color)
        current_numbers = get_number_choices(color_length)

        spelling_label.set_text(color.upper())
        number_label.set_text("Pick a number from " + ", ".join(current_numbers))

        status_label.set_text("Color accepted.")

    else:

        spelling_label.set_text("Invalid color")
        status_label.set_text("Try red, blue, yellow, or green.")


# Purpose: handle number button press
def submit_number():
    global current_numbers, num_selected_once

    number = number_entry.get_text()

    if number in current_numbers:

        if num_selected_once:
            fortune = FORTUNES[number]
            fortune_label.set_text(fortune)
        else:
            current_numbers = get_number_choices_from_number(int(number))
            number_label.set_text("Pick a number from " + ", ".join(current_numbers))
            status_label.set_text("Number accepted.")
            num_selected_once = True
    else:

        fortune_label.set_text("Pick one of the listed numbers.")
        status_label.set_text("Invalid number")


# Purpose: draw the image
def draw_image(surface):

    if image:
        scaled = pygame.transform.scale(image, (320, 320))
        surface.blit(scaled, (180, 500))


# -----------------------------
# MAIN CODE
# -----------------------------
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fortune Teller")

clock = pygame.time.Clock()

manager = pygame_gui.UIManager((WIDTH, HEIGHT))

image = load_image()


# Title
title_label = pygame_gui.elements.UILabel(
    pygame.Rect(140, 20, 420, 30),
    "Pick a color and I will tell your fortune",
    manager
)

# Color instructions
instruction_label = pygame_gui.elements.UILabel(
    pygame.Rect(120, 60, 460, 30),
    "Pick a color: red, blue, yellow, or green",
    manager
)

# Color input
color_entry = pygame_gui.elements.UITextEntryLine(
    pygame.Rect(265, 100, 170, 35),
    manager
)

color_button = pygame_gui.elements.UIButton(
    pygame.Rect(285, 150, 130, 40),
    "Submit color",
    manager
)

# Spelling label (just shows the color)
spelling_label = pygame_gui.elements.UILabel(
    pygame.Rect(250, 210, 200, 30),
    "...",
    manager
)

# Number prompt
number_label = pygame_gui.elements.UILabel(
    pygame.Rect(180, 250, 340, 30),
    "Pick a number from ...",
    manager
)

# Number input
number_entry = pygame_gui.elements.UITextEntryLine(
    pygame.Rect(265, 290, 170, 35),
    manager
)

number_button = pygame_gui.elements.UIButton(
    pygame.Rect(280, 340, 140, 40),
    "Submit number",
    manager
)

# Fortune label
fortune_label = pygame_gui.elements.UILabel(
    pygame.Rect(150, 420, 400, 40),
    "Your fortune will appear here",
    manager
)

# Status label
status_label = pygame_gui.elements.UILabel(
    pygame.Rect(150, 850, 400, 30),
    "",
    manager
)


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