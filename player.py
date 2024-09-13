from settings import *

class Player(pygame.sprite.Sprite):
  def __init__(self, pos, group):
    super().__init__(group)
    self.image = pygame.Surface((48, 56))
    self.image.fill('red')
    self.rect = self.image.get_frect(topleft = pos)

    # Movement
    self.direction = vector()
    self.speed = 200

  def input(self):
    keys = pygame.key.get_pressed()
    input_vector = vector(0, 0)

    if keys[pygame.K_RIGHT]:
      input_vector.x += 1
    if keys[pygame.K_LEFT]:
      input_vector.x -= 1

    self.direction = input_vector.normalize() if input_vector else input_vector

  def move(self, deltaTime):
    self.rect.topleft += self.direction * self.speed * deltaTime


  def update(self, deltaTime):
    self.input()
    self.move(deltaTime)
