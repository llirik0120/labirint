from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Догонялки')
background = transform.scale(image.load('background.jpg'), (700, 500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key. get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 700 - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500 - 80:
            self.rect.y += self.speed

# Class wall(sprite.Sprite):
#     def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_widht, wall_height)
#         super().__init__()
#         self.color_1 = color_1
#         self.color_2 = color_2
#         self.color_3 = color_3
#         self.widht = wall_widht
#         self.height = wall_height
#         self.image = Surface((self.width, self.height))
#         self.image.fill((color_1, color_2, color_3))
#         self.rect = self.image.get_rect()
#         self.rect.x = wall_x
# #         self.rect.y = rect_y

#     def draw_wall(self):
#         window.blit(self.image,(self.rect.x, self.rect.y))

class Enemy(GameSprite):
    direction = 'left'

    def update(self):
        if self.rect.x <= 350:
            self.direction = 'right'
        if self.rect.x >= 700 - 85:       
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

# class wall(sprite.Sprite):
#     def __init__(self, color_1, wall_x, wall_wigth,):
#         super().__init__()
#         self.color_1 = color_1
#         self.wight = wall_widht
#         self.height = wall_height
#         self.image = Surface((self.wight, self.height))
#         self.image.fill((color_1, color_2, color_3))
#         self.rect = self.image.get_rect()
#         self.rect.x = wall_x
#         self.rect.y = wall_y
#     def draw_wall(self):
#         window.blit(self.image, (self.rect.x, self.rect.y))

finish = False
game = True
clock = time.Clock()
FPS = 60

player = Player('hero.png', 100, 100, 7)
monster = Enemy('cyborg.png', 500, 300, 6)
# final = GameSprite('strea.png', )

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        if sprite.collide_rect(player, monster):
            finish = True

        window.blit(background,(0, 0))

        player.update()
        player.reset()
        monster.update()
        monster.reset()

  



    display.update()
    clock.tick(FPS)
