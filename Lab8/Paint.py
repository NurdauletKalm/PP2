import pygame

# pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
COLORS = [BLACK, RED, GREEN, BLUE]

# display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Program")
screen.fill(WHITE)

# Айнымалылар
drawing = False
mode = "қалам"
current_color = BLACK
start_pos = None

# Негізгі код
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                screen.fill(WHITE)  # Clear screen
            elif event.key == pygame.K_r:
                mode = "тіктөртбұрыш"
            elif event.key == pygame.K_o:
                mode = "дөңгелек"
            elif event.key == pygame.K_e:
                mode = "өшіргіш"
            elif event.key == pygame.K_p:
                mode = "қалам"
            elif event.key == pygame.K_1:
                current_color = BLACK
            elif event.key == pygame.K_2:
                current_color = RED
            elif event.key == pygame.K_3:
                current_color = GREEN
            elif event.key == pygame.K_4:
                current_color = BLUE
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            if mode == "тіктөртбұрыш":
                end_pos = event.pos
                rect_width = abs(end_pos[0] - start_pos[0])
                rect_height = abs(end_pos[1] - start_pos[1])
                pygame.draw.rect(screen, current_color, (min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1]), rect_width, rect_height), 2)
            elif mode == "дөңгелек":
                end_pos = event.pos
                radius = int(((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2)**0.5)
                pygame.draw.дөңгелек(screen, current_color, start_pos, radius, 2)
        elif event.type == pygame.MOUSEMOTION and drawing:
            if mode == "қалам":
                pygame.draw.line(screen, current_color, event.pos, event.pos, 5)
            elif mode == "өшіргіш":
                pygame.draw.line(screen, WHITE, event.pos, event.pos, 10)
    
    pygame.display.flip()

pygame.quit()