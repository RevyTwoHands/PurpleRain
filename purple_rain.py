from random import randint

import pygame

# Size of the screen
SCREEN_TITLE = 'Purple Rain'
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 360

# Colors used
BACKGROUND_COLOR = (230, 230, 250)
RAIN_COLOR = (138, 43, 226)
# Clock used to update game events and frames
clock = pygame.time.Clock()


class Drop:

    def __init__(self):
        self.x_pos = randint(0, SCREEN_WIDTH)
        self.y_pos = randint(-500, -50)
        self.width = 2
        self.len = randint(4, 10)
        self.y_speed = randint(4, 10)

    def draw(self, background):
        pygame.draw.line(background, RAIN_COLOR, (self.x_pos, self.y_pos),
                         (self.x_pos, self.y_pos + self.len), self.width)

    def fall(self):
        self.y_pos += self.y_speed
        # Implementing some gravity : the rain starts to fall faster when they get near to the floor
        self.y_speed += 0.05

        # Resetting the rain if it falls out of the screen
        if self.y_pos > SCREEN_HEIGHT:
            self.y_pos = randint(-200, 100)
            self.y_speed = randint(4, 10)


class Game:
    # Corresponding to FPS
    TICK_RATE = 70

    # Initializer for the game class to set up the width, height, and title
    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        # Create the window of specified size in certain colour to display the game
        self.game_screen = pygame.display.set_mode((self.width, self.height))
        # Setting the game window color
        self.game_screen.fill(BACKGROUND_COLOR)
        # Setting the title
        pygame.display.set_caption(self.title)
        pygame.display.update()

    def run_game_loop(self):

        # We create a thousand of rain drops
        rain = []
        for i in range(600):
            rain.append(Drop())

        # Displaying the drops on the screen
        for e in rain:
            e.draw(self.game_screen)
        pygame.display.update()

        while True:
            # A loop to get all the events given at any time
            for event in pygame.event.get():
                # If we have a quit type event (exit out) then exit ou of the game loop
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # Redraw the screen to hide previous position of the drop
            self.game_screen.fill(BACKGROUND_COLOR)
            # We make the drop fall
            for e in rain:
                e.fall()
                e.draw(self.game_screen)
            # Update all game graphics
            pygame.display.update()
            # Tick the clock to update everything within the game
            clock.tick(self.TICK_RATE)


pygame.init()

new_game = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()
