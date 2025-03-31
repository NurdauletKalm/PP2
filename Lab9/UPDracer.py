import pygame
import random

# pygame initialization
pygame.init()

# Variables
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")
clock = pygame.time.Clock()

# Load assets
background = pygame.image.load('road.jpg')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

car_img = pygame.image.load("car.png")
car_width, car_height = car_img.get_size()

coin_img = pygame.image.load("coin.png")
coin_width, coin_height = coin_img.get_size()

enemy_img = pygame.image.load("enemy.png")
enemy_width, enemy_height = enemy_img.get_size()

# Player
player_x = WIDTH // 2 - car_width // 3
player_y = HEIGHT - car_height - 100
player_speed = 5  # You can adjust this for the player's speed

# Coins
coins = []

# Enemies
enemies = []

# Score
score = 0
font = pygame.font.Font(None, 36)

# Function to generate a coin
def generate_coin():
    x = random.randint(50, WIDTH - 50 - coin_width)
    y = random.randint(-10, -5)
    coins.append(pygame.Rect(x, y, coin_width, coin_height))

# Function to move and draw coins
def move_and_draw_coins():
    global score
    for coin in coins[:]:
        coin.y += 1  # Move coins downward
        if coin.colliderect(pygame.Rect(player_x, player_y, car_width, car_height)):
            coins.remove(coin)
            score += random.randint(1, 5)  # Random score increase
        elif coin.y > HEIGHT:
            coins.remove(coin)

# Function to generate enemies
def generate_enemy():
    x = random.randint(50,enemy_width)
    y = random.randint(-10, -5)
    enemies.append(pygame.Rect(x, y, enemy_width//2, enemy_height//2))

# Function to move and draw enemies
def move_and_draw_enemies(speed):
    for enemy in enemies[:]:
        enemy.y += speed  # Move enemies downward
        if enemy.colliderect(pygame.Rect(player_x, player_y, car_width, car_height)):
            print("Game Over!")
            pygame.quit()
            quit()
        elif enemy.y > HEIGHT:
            enemies.remove(enemy)

# Main game loop
running = True
enemy_speed = 1  # Initial enemy speed

while running:
    screen.fill(WHITE)
    screen.blit(background, (0, 0))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - car_width:
        player_x += player_speed

    # Generate coins and enemies
    if random.randint(1, 50) == 1:  # Chance to generate a coin
        generate_coin()
    if random.randint(1, 250) == 1:  # Chance to generate an enemy
        generate_enemy()

    # Adjust enemy speed based on score
    if score >= 10:
        enemy_speed = 2
    if score >= 20:
        enemy_speed = 3
    if score >= 30:
        enemy_speed = 4

    # Move coins and enemies
    move_and_draw_coins()
    move_and_draw_enemies(enemy_speed)

    # Draw player car, coins, and enemies
    screen.blit(car_img, (player_x, player_y))
    for coin in coins:
        screen.blit(coin_img, (coin.x, coin.y))
    for enemy in enemies:
        screen.blit(enemy_img, (enemy.x, enemy.y))

    # Display score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (WIDTH - 150, 20))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
