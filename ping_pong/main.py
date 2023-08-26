from pygame import*

WIDTH = 700
HEIGHT = 500

BG_COLOR = (137, 207, 240)
WHITE = (255,255,255)
RED = (255,10,10)
BLUE =(0, 180, 255)

dx = 3
dy = 3

screen = display.set_mode((WIDTH, HEIGHT))
display.set_caption("ping-pong game")
clock = time.Clock()
background = transform.scale(image.load("court.jpeg"),(WIDTH,HEIGHT))

class Gamesprite(sprite.Sprite):
    def __init__(self, img, x, y, width,height, speed):
        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(img), (width, height))
        self.speed = speed

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))


class Player(Gamesprite):
    def controls_Left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500 - 100:
            self.rect.y += self.speed
    def controls_Right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500 - 100:
            self.rect.y += self.speed

player_1 = Player("racket.png", 25, 250, 25, 80, 10)
player_2 = Player("racket.png", 650, 250, 25, 80, 10)
ball = Gamesprite("ball.png", 350, 250, 40, 40, 10)


score_1 = 0
score_2 = 0

font.init()
style = font.Font(None, 45)
player_1_text = style.render(str(score_1), True, (0,0,0))
player_2_text = style.render(str(score_2), True, (0,0,0))


end = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False




    if end != True:
        screen.blit(background,(0,0))
        player_1.reset()
        player_2.reset()
        ball.reset()

        player_1.controls_Left()
        player_2.controls_Right()



        ball.rect.x += dx
        ball.rect.y += dy


        if ball.rect.y > HEIGHT-50 or ball.rect.y < 50:
            dy *= -1

        
        if player_2.rect.colliderect(ball.rect):
            dx *= -1

        if player_1.rect.colliderect(ball.rect):
            dx *= -1
        
        if ball.rect.x < 0:
            score_2 += 1
            ball = Gamesprite("ball.png", 350, 250, 40, 40, 10)
            player_2_text = style.render(str(score_2), True, (0,0,0))      


        if ball.rect.x > 700:
            score_1 += 1
            ball = Gamesprite("ball.png", 350, 250, 40, 40, 10)
            player_1_text = style.render(str(score_1), True, (0,0,0))




        if score_1 >= 5 or score_2 >= 5:
            end = True

        if score_1 >= 5:
            win_text = style.render("Player 1 Wins!", True,(10,250,10))
            screen.blit(win_text, (WIDTH//2,HEIGHT//2))

        if score_2 >= 5:
            win_text = style.render("Player 2 Wins!", True,(10,250,10))
            screen.blit(win_text, (WIDTH//2,HEIGHT//2))

        screen.blit(player_1_text, (10, 25))
        screen.blit(player_2_text, (675, 25))
    
        display.update()

    else:
        end = False
        score_1 = 0
        score_2 = 0
        time.delay(3000)


    clock.tick(40)
