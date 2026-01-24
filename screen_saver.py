# screensaver lesson
# steps
# 1. create a window and title
# 2. create game loop with tick(), 60 fps
# 3. draw static text
# 4. animate the text horizontally
# 5. bounce text off side walls
# 6. animate text vertically, bounce off top and bottom
# 7. animate text diagonally
# 8. add other bouncing effects: color, speed, text change
# 9. you're done!

# load pygame library
import pygame
# load random library
import random

# constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
TEXT_MESSAGE = "Hello Isabelle!"
FPS_MAX = 60 # games are typically 60 frames per second

# bouncing text velocity
x_velocity = 110
y_velocity = 90

# starts pygame internal systems
pygame.init()

# opens a window
# screen is where you draw
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# set window title
pygame.display.set_caption("Hello Pygame")

# create FPS limiter stopwatch
clock = pygame.time.Clock()

# text
# default font, 48 pixels tall
font = pygame.font.SysFont(None, 48)
# convert font to an image (surface object), anti-aliasing True
color = (255, 255, 255)
text = font.render(TEXT_MESSAGE, True, color)
# creates rect for text and centers it in screen
# tells pygame where to draw it
text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))


# game loop
running = True
while running:
    # handle events (input)
    for event in pygame.event.get():
        # quit event
        if event.type == pygame.QUIT:
            running = False

    # pace the loop (limit FPS)
    # if computer is too fast, it pauses to maintain FPS
    # target is 1/60, but actual value is variable
    delta_time = clock.tick(FPS_MAX) / 1000 # seconds

    # for animation
    # speed = pixels per second (not pixels per frame)
    # time = seconds per frame
    # distance = pixels to move per frame
    # distance = speed x time
    # x += speed * secs_since_last_frame

    # move text
    text_rect.x += x_velocity * delta_time
    text_rect.y += y_velocity * delta_time

    # bounce off left and right walls
    if text_rect.left < 0 or text_rect.right > SCREEN_WIDTH:
        x_velocity *= -1
        # set random color
        color = (
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255),
        )
    
    # bounce off top and bottom walls
    if text_rect.top < 0 or text_rect.bottom > SCREEN_HEIGHT:
        y_velocity *= -1
        # set random color
        color = (
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255),
        )

    text = font.render(TEXT_MESSAGE, True, color)

    # update state
    # fill screen with dark gray
    screen.fill((30, 30, 30))
    # draw text at this centered rect position
    screen.blit(text, text_rect)

    # draw
    # update display
    # shows everything we drew in this frame
    pygame.display.flip()

    

# quit
# clean exit once exit game loop
pygame.quit()
