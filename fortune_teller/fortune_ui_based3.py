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
HEIGHT = 800
FPS = 60
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

COLORS = ["red", "blue", "green", "yellow"]

set1 = ["1", "2", "5", "6"]             # same names as text version
set2 = ["3", "4", "7", "8"]

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
# GAME STATE (changes during play)
# -----------------------------
current_set = set1
num_selected_once = False


# -----------------------------
# FUNCTIONS
# -----------------------------

# ✅ SAME as text version
def flip_numbers(current_set):
    if current_set == set1:
        return set2
    else:
        return set1


# ✅ SAME as text version
def get_starting_set(color):
    if len(color) % 2 == 0:
        return set1
    else:
        return set2


# ✅ SAME as text version
def get_fortune(number):
    return fortunes[number - 1]


# Purpose: load an image file
def load_image(filename):
    try:
        image_path = os.path.join(BASE_DIR, filename)
        return pygame.image.load(image_path)
    except:
        return None


# Purpose: handle color submission
def submit_color():
    global current_set, num_selected_once

    color = color_entry.get_text().lower().strip()

    # ✅ Same logic call as text version: current_set = get_starting_set(color)
    current_set = get_starting_set(color)
    num_selected_once = False

    color_label.set_text("You chose: " + color.upper())
    number_label.set_text("Pick a number from: " + ", ".join(current_set))
    fortune_label.set_text("Your fortune will appear here")
    number_entry.set_text("")
    status_label.set_text("Now choose your first number.")


# Purpose: handle number submission
def submit_number():
    global current_set, num_selected_once

    number = int(number_entry.get_text().strip())

    if num_selected_once:
        # ✅ Same logic call as text version: get_fortune(second_choice)
        fortune_label.set_text("🔮 Your fortune: " + get_fortune(number))
        status_label.set_text("Fortune revealed!")
    else:
        # ✅ Same logic call as text version: flip_numbers(current_set)
        current_set = flip_numbers(current_set)
        number_label.set_text("Pick ANOTHER number from: " + ", ".join(current_set))
        number_entry.set_text("")
        num_selected_once = True
        status_label.set_text("Choose one more number.")


# Purpose: draw the image
def draw_image(surface):
    if image:
        scaled = pygame.transform.scale(image, (280, 280))
        surface.blit(scaled, (210, 480))


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
    "Magic Fortune Teller",
    manager
)

# Instructions
instruction_label = pygame_gui.elements.UILabel(
    pygame.Rect(70, 60, 560, 30),
    "Choose a color, then a number, then one more number to reveal your fortune!",
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
    pygame.Rect(100, 770, 500, 30),
    "Type a color to begin.",
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
