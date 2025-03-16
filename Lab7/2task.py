import pygame
import os

music_folder = "music"
playlist = [os.path.join(music_folder, file) for file in os.listdir(music_folder) if file.endswith(".mp3")]
current_track = 0

def play():
  if playlist:
    pygame.mixer.music.load(playlist[current_track])
    pygame.mixer.music.play(0)
    
def stop():
  pygame.mixer.music.stop()

def next_track():
  global current_track
  current_track = (current_track + 1) % len(playlist)
  play()

def previous_track():
  global current_track
  current_track = (current_track - 1) % len(playlist)
  play()

pygame.init()
pygame.mixer.init()

pygame.font.init()
font = pygame.font.SysFont("Arial", 24)

done = False
clock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 200))

while not done:
  clock.tick(60)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True

  screen.fill((255, 255, 255))
  pressed = pygame.key.get_pressed() 
  if pressed[pygame.K_SPACE]: stop() #stop
  if pressed[pygame.K_o]: play() #play
  if pressed[pygame.K_RIGHT]: next_track() #next
  if pressed[pygame.K_LEFT]: previous_track() #previous

  if playlist:
        track_name = os.path.basename(playlist[current_track])
        text_surface = font.render(f"Playing: {track_name}", True, (0, 0, 0))
        screen.blit(text_surface, (50, 80))

  pygame.display.flip()
pygame.quit()