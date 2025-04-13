#Создай собственный Шутер!

from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed): 
        super().__init__()
        self.image = transform.scale(image.load(player_image), (50, 100))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

window = display.set_mode((500, 600))
display.set_caption("Шутер")


class player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
    def update(self):

        keys_pressed = key.get_pressed()
        
        if keys_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 450:
            self.rect.x += self.speed

    def fire(self):
        bullet = Bullet('bullet.png', self.rect.x, self.rect.top, 2)        
        Bullets = sprite.Group()
        Bullets.add(bullet)
        Bullets.update()
good_sprite = player("jeep.png", 200, 500, 2)

class enemy(GameSprite):
    def update(self):
        if self.rect.y >= 510:
           self.rect.y = 0
           self.rect.x = randint(50, 400)
        elif self.rect.y < 510:
           self.rect.y += self.speed

zombie = enemy('zombie1.png', 100, 50, 1) 

sprites = sprite.Group()
sprites.add(enemy('zombie1.png', 50, 50, 1) )
sprites.add(enemy('zombie1.png', 200, 50, 1) )
sprites.add(enemy('zombie1.png', 100, 50, 1) )
sprites.add(enemy('zombie1.png', 300, 50, 1) )



class Bullet(GameSprite):
    def update(self):
        if self.rect.y > 0:
            self.rect.y -= self.speed
        elif self.rect.y <= 0:
            self.kill
            








background = transform.scale(image.load("GRASS.jpg"), (500, 600) )



clock = time.Clock()
FPS = 60
clock.tick(FPS)



mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

game = True
while game:
    window.blit(background, (0, 0))
    good_sprite.reset()
    good_sprite.update()
    zombie.reset()
    zombie.update()
    sprites.draw(window)
    sprites.update()
    good_sprite.fire()
    
  

    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()