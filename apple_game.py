import pygame
import math
import random


#pygame initialise
pygame.init()

#create screen
screen = pygame.display.set_mode((500, 500))

#Set Title
pygame.display.set_caption("leaves FALLING")

#Set Icon
icon = pygame.image.load("leaf.png")
pygame.display.set_icon(icon)

bg = pygame.image.load('a.png')

golden_leaf_count = 0

score = 0
scoreFont = pygame.font.Font("freesansbold.ttf", 20)


def showScore():
  ss = scoreFont.render("Score: " + str(score), True, "black")
  screen.blit(ss, (0, 0))


class Leaf:

  def __init__(self):
    self.img = pygame.image.load('leaf.png')
    self.x = 0
    self.y = 0

  def display(self):
    screen.blit(self.img, (self.x, self.y))
    self.y += 3
    xc = 0

    if self.y > 600:
      xc+=1
      self.y = 0
      self.x = random.randint(0, 775)
      if xc == 10:
        self.img = pygame.image.load("tropical-leaves.png")
        self.name = "green"
      else:
        self.img = pygame.image.load("leaf.png")
        self.name = "leaf"


class bascket:

  def __init__(self):
    self.img = pygame.image.load('wicker-basket.png')
    self.x = 380
    self.y = 300
    self.x_change = 0

  def display(self):
    screen.blit(self.img, (self.x, self.y))


def iscollision(ufo_x, ufo_y, player_x, player_y):
  global score
  d = math.dist((Basket.x, Basket.y), (leaf.x, leaf.y))
  if d < 40:
    return True


leaf = Leaf()
Basket = bascket()
while True:
  screen.blit(bg, (0, 0))
  showScore()
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        Basket.x_change = -3
      elif event.key == pygame.K_RIGHT:
        Basket.x_change = 3
    elif event.type == pygame.KEYUP:
      Basket.x_change = 0

  if Basket.x > 430:
    Basket.x = 430
  elif Basket.x < 0:
    Basket.x = 0
  Basket.x += Basket.x_change
  leaf.display()
  Basket.display()

  if iscollision(Basket.x, Basket.y, leaf.x, leaf.y):
    leaf.x = random.randint(0, 775)
    leaf.y = 0
    if leaf.name == "leaf":  
      score+=1
    elif leaf.name == "green":
      score = 0

  pygame.display.update()
