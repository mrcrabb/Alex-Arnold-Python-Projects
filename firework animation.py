import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Firework Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

# Particle class
class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.radius = random.randint(2, 4)
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = random.uniform(1, 5)
        self.lifetime = random.randint(20, 40)
        self.age = 0

    def move(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed
        self.age += 1

    def is_alive(self):
        return self.age < self.lifetime

    def draw(self):
        alpha = max(0, 255 - (self.age / self.lifetime) * 255)
        color = (*self.color, alpha)
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), self.radius)

# Firework class
class Firework:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = HEIGHT
        self.color = random.choice(COLORS)
        self.particles = []
        self.exploded = False

    def explode(self):
        for _ in range(100):
            particle = Particle(self.x, self.y, self.color)
            self.particles.append(particle)
        self.exploded = True

    def update(self):
        if not self.exploded:
            self.y -= 5
            if self.y <= random.randint(100, 300):
                self.explode()
        else:
            for particle in self.particles:
                particle.move()

    def is_alive(self):
        return not self.exploded or any(particle.is_alive() for particle in self.particles)

    def draw(self):
        if not self.exploded:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 5)
        else:
            for particle in self.particles:
                particle.draw()

# Main loop
clock = pygame.time.Clock()
fireworks = []

running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Add new firework
    if random.random() < 0.05:
        fireworks.append(Firework())

    # Update and draw fireworks
    for firework in fireworks:
        firework.update()
        firework.draw()

    # Remove dead fireworks
    fireworks = [firework for firework in fireworks if firework.is_alive()]

    pygame.display.flip()
    clock.tick(30)

pygame.quit()