import pygame
import random

# pygame
pygame.init()

# Айнымалылар
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

#display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")
clock = pygame.time.Clock()

# assets
car_img = pygame.image.load("car.png") 
car_width, car_height = car_img.get_size()

# ойыншы
player_x = WIDTH // 2 - car_width // 2
player_y = HEIGHT - car_height - 20
player_speed = 5

# Тиын
coin_img = pygame.image.load("coin.png")  # Load coin image
coin_width, coin_height = coin_img.get_size()
coins = []

# Score
score = 0
font = pygame.font.Font(None, 36)

#random coin
def generate_coin():
    x = random.randint(50, WIDTH - 50 - coin_width)
    y = random.randint(-500, -50)
    coins.append(pygame.Rect(x, y, coin_width, coin_height))

def draw_coins():
    for coin in coins:
        screen.blit(coin_img, (coin.x, coin.y))

def move_coins():
    global score
    for coin in coins[:]:
        coin.y += 1  # Move coins downward
        if coin.colliderect(pygame.Rect(player_x, player_y, car_width, car_height)):
            coins.remove(coin)
            score += 1  # Increase score on collection
        elif coin.y > HEIGHT:
            coins.remove(coin)
#басты код
running = True
while running:
    screen.fill(WHITE)
    
    # Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - car_width:
        player_x += player_speed
    
    # random coins
    if random.randint(1, 1000) == 1:
        generate_coin()
    
    move_coins()
    
    #player car
    screen.blit(car_img, (player_x, player_y))
    draw_coins()
    
    #score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (WIDTH - 150, 20))
    
    pygame.display.flip()

pygame.quit()
