# Import modules

import pygame
import time
from buttons import Buttons
from textwrap import dedent

__version__ = "1.0.0"

# Initialize
try:
    pygame.init()
except pygame.error:
    # Getting this error when module isn't initialize
    raise SystemExit("Pygame couldn't initialize.")

# Create window
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Pygame Buttons")

# Error when window could not be created
if screen is None:
    raise SystemExit("Pygame couldn't create window.")

font = pygame.font.SysFont("Arial", 50, bold = False)

version_font = font.render(f"v{__version__}", True, "black")

print(dedent(
    f"""\
        Welcome to Pygame buttons!
        Version: v{__version__}
        Thank you for using Pygame buttons!
    """
))

elapsed_time = 0
start_time = time.time()

play_button = Buttons(screen.get_width() / 3 - (252 / 2), 170, 150, 75, "resources/play.png", "resources/play_hover.png")
quit_button = Buttons(screen.get_width() / 1.2 - (252 / 2), 170, 150, 75, "resources/quit.png", "resources/quit_hover.png")

clock = pygame.time.Clock()

def main():
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            # Quitting the game means when clicked on "X" button
            if event.type == pygame.QUIT:
                print("quitting")
                time.sleep(1)
                print(f"took in {round(elapsed_time)}s")
                running = False
            
            if event.type == pygame.USEREVENT and event.button == quit_button:
                print("quitting")
                time.sleep(1)
                print(f"took in {round(elapsed_time)}s")
                running = False

            # Or means when clicked on quit button
            quit_button.event_handling(event)
        
        # Drawing
        screen.fill((20, 156, 204))
        # Drawing buttons
        play_button.draw(screen)
        quit_button.draw(screen)
        # Update method
        play_button.check_hover(pygame.mouse.get_pos())
        quit_button.check_hover(pygame.mouse.get_pos())
        screen.blit(version_font, (1, 1))
        elapsed_time = time.time() - start_time
        pygame.display.update()
        clock.tick(60)

    # Uninitialize
    pygame.quit()

if __name__ == "__main__":
    main()