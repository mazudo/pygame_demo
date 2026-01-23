# virtual pet. click the buttons to care for it
# mood changes with time 

# import necessary libraries
import os
import sys
import pygame
import pygame_gui

# Import specific UI elements we will use
from pygame_gui.elements import UIButton, UILabel, UIProgressBar

# -----------------------------
# File / asset helpers
# -----------------------------

# Folder where images live
ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")

def load_png(path):
    """
    Load a PNG image with transparency.
    If the file is missing, crash with a helpful error message.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Missing image: {path}")
    return pygame.image.load(path).convert_alpha() # return as an efficient Surface

def scale_to_fit(img, max_w, max_h):
    """
    Scale an image to fit inside a box while keeping aspect ratio.
    """
    w, h = img.get_size()
    scale = min(max_w / w, max_h / h)
    new_size = (int(w * scale), int(h * scale))
    return pygame.transform.smoothscale(img, new_size)

def clamp(value, min_val, max_val):
    """
    Keep a number between min_val and max_val.
    """
    return max(min_val, min(max_val, value))

def mood_from_happiness(happiness):
    """
    Convert a numeric happiness value into a mood name.
    """
    if happiness <= 32:
        return "sad"
    elif happiness <= 66:
        return "content"
    else:
        return "happy"

# -----------------------------
# Main game function
# -----------------------------

# def main():
# init pygame and set caption
pygame.init()
pygame.display.set_caption("Virtual Pet – Happiness Demo")

# Window size
WIDTH, HEIGHT = 900, 560
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# fps clock
clock = pygame.time.Clock()

# pygame_gui manages UI widgets & events
manager = pygame_gui.UIManager((WIDTH, HEIGHT))

# -----------------------------
# Pet display area (left side)
# -----------------------------
PET_AREA = pygame.Rect(20, 20, 580, 520)
IMAGE_PADDING = 40

# Load and scale pet images
sad_img = scale_to_fit(
    load_png(os.path.join(ASSETS_DIR, "pet_sad.png")),
    PET_AREA.width - IMAGE_PADDING,
    PET_AREA.height - IMAGE_PADDING
)

content_img = scale_to_fit(
    load_png(os.path.join(ASSETS_DIR, "pet_content.png")),
    PET_AREA.width - IMAGE_PADDING,
    PET_AREA.height - IMAGE_PADDING
)

happy_img = scale_to_fit(
    load_png(os.path.join(ASSETS_DIR, "pet_happy.png")),
    PET_AREA.width - IMAGE_PADDING,
    PET_AREA.height - IMAGE_PADDING
)

# Store images in a dictionary by mood
pet_images = {
    "sad": sad_img,
    "content": content_img,
    "happy": happy_img
}

# -----------------------------
# Pet state variables
# -----------------------------
happiness = 40              # Start in the "content" range
mood = mood_from_happiness(happiness)
current_pet_image = pet_images[mood]

# -----------------------------
# UI panel (right side)
# -----------------------------
panel_x = 620
panel_width = WIDTH - panel_x - 20

UILabel(
    pygame.Rect((panel_x, 20), (panel_width, 30)),
    "Pet Controls",
    manager
)

mood_label = UILabel(
    pygame.Rect((panel_x, 60), (panel_width, 30)),
    f"Mood: {mood}",
    manager
)

happiness_label = UILabel(
    pygame.Rect((panel_x, 95), (panel_width, 25)),
    f"Happiness: {int(happiness)} / 100",
    manager
)

# Progress bar shows happiness visually
happiness_bar = UIProgressBar(
    pygame.Rect((panel_x, 125), (panel_width, 25)),
    manager
)
# progress bar between 0.0 - 100.0
happiness_bar.set_current_progress(int(happiness))

# Buttons
# feed button
feed_button = UIButton(
    pygame.Rect((panel_x, 170), (panel_width, 45)),
    "Feed (+10)",
    manager
)
# play button
play_button = UIButton(
    pygame.Rect((panel_x, 225), (panel_width, 45)),
    "Play (+15)",
    manager
)
# pet button
pet_button = UIButton(
    pygame.Rect((panel_x, 280), (panel_width, 45)),
    "Pet (+5)",
    manager
)

# -----------------------------
# Happiness update logic
# -----------------------------
def change_happiness(amount):
    """
    Change happiness, update UI, and swap pet image if mood changes.
    """
    global happiness, mood, current_pet_image

    # Update value safely
    happiness = clamp(happiness + amount, 0, 100)

    # Update text + progress bar
    happiness_label.set_text(f"Happiness: {int(happiness)} / 100")
    happiness_bar.set_current_progress(int(happiness))

    # Check if mood changed
    new_mood = mood_from_happiness(happiness)
    if new_mood != mood:
        mood = new_mood
        mood_label.set_text(f"Mood: {mood}")
        current_pet_image = pet_images[mood]

# Optional: happiness slowly decreases over time
HAPPINESS_DECAY_PER_SECOND = 1.0

# -----------------------------
# Main loop
# -----------------------------
running = True
while running:
    dt = clock.tick(60) / 1000  # Delta time in seconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Let pygame_gui handle UI events
        manager.process_events(event)

        # Button clicks
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == feed_button:
                change_happiness(+10)
            elif event.ui_element == play_button:
                change_happiness(+15)
            elif event.ui_element == pet_button:
                change_happiness(+5)

    # Apply slow decay
    if HAPPINESS_DECAY_PER_SECOND > 0:
        change_happiness(-HAPPINESS_DECAY_PER_SECOND * dt)

    # Update UI system
    manager.update(dt)

    # -----------------------------
    # Draw everything
    # -----------------------------

    # background color
    screen.fill((24, 24, 30))

    # Pet background panel
    pygame.draw.rect(screen, (40, 40, 50), PET_AREA, border_radius=12)

    # Draw current pet image centered
    pet_rect = current_pet_image.get_rect(center=PET_AREA.center)
    screen.blit(current_pet_image, pet_rect)

    # Draw UI on top
    manager.draw_ui(screen)

    pygame.display.flip()

pygame.quit()

# -----------------------------
# Program entry point
# -----------------------------
# if __name__ == "__main__":
#     try:
#         main()
#     except Exception as e:
#         print(e)
#         sys.exit(1)
