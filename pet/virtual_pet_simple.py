import os
import pygame
import pygame_gui
from pygame_gui.elements import UIButton, UIProgressBar, UILabel

# Initialize pygame
pygame.init()
pygame.display.set_caption("Virtual Pet")

# Window size
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
manager = pygame_gui.UIManager((WIDTH, HEIGHT))

# Load pet images
ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")

def load_png(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Missing image: {path}")
    return pygame.image.load(path).convert_alpha()

def scale_to_fit(img, max_w, max_h):
    w, h = img.get_size()
    scale = min(max_w / w, max_h / h)
    new_size = (int(w * scale), int(h * scale))
    return pygame.transform.smoothscale(img, new_size)

def clamp(value, min_val, max_val):
    return max(min_val, min(max_val, value))

def mood_from_happiness(happiness):
    if happiness <= 32:
        return "sad"
    elif happiness <= 66:
        return "content"
    else:
        return "happy"

# Load and scale pet images
sad_img = scale_to_fit(load_png(os.path.join(ASSETS_DIR, "pet_sad.png")), 250, 200)
content_img = scale_to_fit(load_png(os.path.join(ASSETS_DIR, "pet_content.png")), 250, 200)
happy_img = scale_to_fit(load_png(os.path.join(ASSETS_DIR, "pet_happy.png")), 250, 200)

# Store images in a dictionary by mood
pet_images = {
    "sad": sad_img,
    "content": content_img,
    "happy": happy_img
}

# Pet state
happiness = 100  # Start at max happiness (happy mood)
mood = mood_from_happiness(happiness)
current_pet_image = pet_images[mood]

# Happiness decay over time
HAPPINESS_DECAY_PER_SECOND = 15.0  # Decreases 15 points per second

# Create mood message label
mood_message = {
    "happy": "I am happy!",
    "content": "I am content",
    "sad": "I am sad, please pet me"
}
mood_label = UILabel(
    pygame.Rect((50, 160), (300, 25)),
    mood_message[mood],
    manager
)

# Create happiness label
happiness_label = UILabel(
    pygame.Rect((50, 190), (300, 25)),
    "Happiness",
    manager
)

# Create progress bar
happiness_bar = UIProgressBar(
    pygame.Rect((50, 220), (300, 20)),
    manager
)
happiness_bar.set_current_progress(happiness)

# Create button
button = UIButton(
    pygame.Rect((150, 250), (100, 40)),
    "Pet Me!",
    manager
)

# Main loop
running = True
while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        manager.process_events(event)

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == button:
                happiness = clamp(happiness + 25, 0, 100)

    # Apply decay over time
    happiness = clamp(happiness - HAPPINESS_DECAY_PER_SECOND * dt, 0, 100)
    
    # Update progress bar
    happiness_bar.set_current_progress(happiness)
    
    # Update mood if it changed
    new_mood = mood_from_happiness(happiness)
    if new_mood != mood:
        mood = new_mood
        current_pet_image = pet_images[mood]
        mood_label.set_text(mood_message[mood])

    manager.update(dt)

    # Draw
    screen.fill((24, 24, 30))
    
    image_rect = current_pet_image.get_rect(center=(WIDTH // 2, 100))
    screen.blit(current_pet_image, image_rect)
    
    manager.draw_ui(screen)
    pygame.display.flip()

pygame.quit()
