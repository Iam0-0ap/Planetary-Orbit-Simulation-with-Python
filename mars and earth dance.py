import pygame
import math
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1920, 1080
XC, YC = WIDTH // 2, HEIGHT // 2
SUN_RADIUS = 50
EARTH_RADIUS = 25
EARTH_ORBIT_RADIUS = 220
MARS_RADIUS = 15
MARS_ORBIT_RADIUS = 320
EARTH_SPEED = 1
MARS_SPEED = 1 / (1 + math.sqrt(5))
ANGLE_CHANGE = -0.05

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 165, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Create the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mars and Earth Dance")
clock = pygame.time.Clock()

def draw_sun():
    pygame.draw.circle(screen, YELLOW, (XC, YC), SUN_RADIUS)

def draw_earth(earth_x, earth_y):
    pygame.draw.circle(screen, BLUE, (earth_x, earth_y), EARTH_RADIUS)

def draw_mars(mars_x, mars_y):
    pygame.draw.circle(screen, RED, (mars_x, mars_y), MARS_RADIUS)

class Animation:
    def __init__(self):
        self.lines_buffer = pygame.Surface((WIDTH, HEIGHT))

    def draw_lines(self):
        for i in range(0, len(lines), 4):
            pygame.draw.line(screen, WHITE, (lines[i], lines[i+1]), (lines[i+2], lines[i+3]))

def main():
    running = True
    global angle, count, lines
    angle = 0
    count = 0
    lines = []

    animation = Animation()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill(BLACK)

        # Draw the orbits
        pygame.draw.circle(screen, WHITE, (XC, YC), EARTH_ORBIT_RADIUS, 1)
        pygame.draw.circle(screen, WHITE, (XC, YC), MARS_ORBIT_RADIUS, 1)

        earth_x = int(XC + EARTH_ORBIT_RADIUS * math.cos(angle * EARTH_SPEED))
        earth_y = int(YC + EARTH_ORBIT_RADIUS * math.sin(angle * EARTH_SPEED))
        mars_x = int(XC + MARS_ORBIT_RADIUS * math.cos(angle * MARS_SPEED))
        mars_y = int(YC + MARS_ORBIT_RADIUS * math.sin(angle * MARS_SPEED))

        if count % 5 == 0:
            lines.extend([earth_x, earth_y, mars_x, mars_y])

        # Draw the planets
        draw_earth(earth_x, earth_y)
        draw_mars(mars_x, mars_y)

        # Update and draw animation
        animation.draw_lines()

        angle += ANGLE_CHANGE
        count += 1

        pygame.display.update()

        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()