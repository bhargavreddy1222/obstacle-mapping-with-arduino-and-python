import pygame
import math
import serial
import time

MAX_DIST = 100
WIDTH, HEIGHT = 700, 700
RADIUS = 350
CENTER = (WIDTH // 2 - 10, HEIGHT // 2 + 100)

try:
    ser = serial.Serial('COM7', 9600, timeout=0.05)
    time.sleep(2)
    print("Serial Connected")
except:
    ser = None
    print("Serial connection failed")


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Radar Scanner")
clock = pygame.time.Clock()

radar_base = pygame.Surface((WIDTH, HEIGHT))
radar_base.fill((0, 0, 0))

for r in range(50, RADIUS, 50):
    pygame.draw.circle(radar_base, (0, 80, 0), CENTER, r, 1)

for a in range(0, 181, 30):
    x = CENTER[0] + RADIUS * math.cos(math.radians(a))
    y = CENTER[1] - RADIUS * math.sin(math.radians(a))
    pygame.draw.line(radar_base, (0, 80, 0), CENTER, (x, y), 1)


fade_surface = pygame.Surface((WIDTH, HEIGHT))
fade_surface.set_alpha(25)      # lower = longer trail
fade_surface.fill((0, 0, 0))

angle = 0.0
distance = MAX_DIST


def read_serial():
    if not ser:
        return None, None
    try:
        line = ser.readline().decode(errors="ignore").strip()
        if "," not in line:
            return None, None
        a, d = line.split(",")
        return float(a), float(d)
    except:
        return None, None


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    new_angle, new_dist = read_serial()
    if new_angle is not None:
        angle = new_angle
        distance = new_dist


    screen.blit(fade_surface, (0, 0))


    screen.blit(radar_base, (0, 0))

    # Sweep line
    sx = CENTER[0] + RADIUS * math.cos(math.radians(angle))
    sy = CENTER[1] - RADIUS * math.sin(math.radians(angle))
    pygame.draw.line(screen, (0, 255, 0), CENTER, (sx, sy), 3)

    # Obstacle
    if distance < MAX_DIST:
        scaled = (distance / MAX_DIST) * RADIUS
        ox = CENTER[0] + scaled * math.cos(math.radians(angle))
        oy = CENTER[1] - scaled * math.sin(math.radians(angle))

        # GREEN line BELOW the dot 
        pygame.draw.line(screen, (0, 255, 0), CENTER, (ox, oy), 2)

        # RED dot
        pygame.draw.circle(screen, (255, 0, 0), (int(ox), int(oy)), 8)
        
        #red line ABOVE the dot
        pygame.draw.line(screen, (255, 0, 0), (ox, oy), (sx, sy), 2)


  
    font = pygame.font.SysFont("consolas", 22)
    txt = font.render(
        f"Angle: {int(angle)}°   Distance: {int(distance)} cm",
        True,
        (0, 255, 0)
    )
    screen.blit(txt, (50, 40))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
