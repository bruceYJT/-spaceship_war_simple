import pygame,random,sys

class Window:
    def __init__(self,win_height,win_width,title,background_url):
        self.win_height = win_height
        self.win_width = win_width
        self.title = title
        self.bg = pygame.image.load(background_url)
        self.window = pygame.display.set_mode((self.win_width,self.win_height))
    def update(self):
        self.window.blit(self.bg, (0,0))
        self.scope = 0

class Hero:
    def __init__(self,img_url,window):
        self.window = window
        self.img = pygame.image.load(img_url)
        self.rect = self.img.get_rect()
        self.rect.centerx = window.win_width/2
        self.rect.bottom = window.win_height - 10
        self.bullet_list = []
        self.active = True
        self.kill_delay = 5
        self.kill_loop = 0
        self.kill_img_list = ['regularExplosion00.png','regularExplosion01.png','regularExplosion02.png','regularExplosion03.png','regularExplosion04.png','regularExplosion05.png','regularExplosion06.png','regularExplosion07.png','regularExplosion08.png']

    def plain(self):
        keyPress = pygame.key.get_pressed()
        if keyPress[pygame.K_a] and self.rect.left > 0:
            # hero_rect.left = hero_rect.left - 10
            self.rect = self.rect.move(-10,0)
        if keyPress[pygame.K_d] and self.rect.right < self.window.win_width:
            self.rect = self.rect.move(10,0)

    def shoot(self,speed):
        self.bullet_list.append(Bullet('./img/laserRed16.png',self.window,self,speed))
        for i in self.bullet_list:
            if not i.active:
                self.bullet_list.remove(i)
    
    def kill(self):
        self.active = False

    def update(self):
        if self.active:
            self.window.window.blit(self.img,self.rect)
        else:
            self.kill_loop += 1
            if self.kill_loop <= (len(self.kill_img_list) - 1)*self.kill_delay:
                self.img = pygame.image.load('./img/' + self.kill_img_list[self.kill_loop//self.kill_delay])
                self.window.window.blit(self.img,self.rect)
            else:
                sys.exit()
        for i in self.bullet_list:
            i.fly()
            i.update()


class Bullet:
    def __init__(self,img_url,window,hero,speed):
        self.window = window
        self.hero = hero
        self.img = pygame.image.load(img_url)
        self.rect = self.img.get_rect()
        self.rect.bottom = self.hero.rect.top
        self.rect.centerx = self.hero.rect.centerx
        self.speed = speed
        self.active = True

    def fly(self):
        self.rect.top -= self.speed
        if self.rect.bottom <= 0:
            self.active = False

    def kill(self):
        self.active = False

    def update(self):
        if self.active:
            self.window.window.blit(self.img,self.rect)


class Enemy:
    def __init__(self,img_url,window):
        self.window = window
        self.img = pygame.image.load(img_url)
        self.rect = self.img.get_rect()
        self.rect.centerx = random.randint(50,750)
        self.rect.top = -50
        self.active = True
        self.speed = 5
        self.kill_delay = 5
        self.kill_loop = 0
        self.kill_img_list = ['sonicExplosion00.png','sonicExplosion01.png','sonicExplosion04.png','sonicExplosion05.png','sonicExplosion06.png','sonicExplosion07.png']
        self.killed = False

    def fly(self):
        if self.active:
            self.rect = self.rect.move(0,self.speed)
        if self.rect.top >= self.window.win_height:
            self.active = False
    
    def colliderect(self,e):
        if self.active and self.rect.colliderect(e.rect):
            self.active = False
            self.killed = True
            self.rect = self.rect.move(-50,-50)
            e.kill()


    def update(self):
        if self.active:
            self.window.window.blit(self.img,self.rect)
        elif self.killed == True:
            self.kill_loop += 1
            if self.kill_loop <= (len(self.kill_img_list) - 1)*self.kill_delay:
                self.img = pygame.image.load('./img/' + self.kill_img_list[self.kill_loop//self.kill_delay])
                self.window.window.blit(self.img,self.rect)
            else:
                self.window.scope += 50




class Brown:
    def __init__(self,img_parent_url,window):
        self.window = window
        self.img_list = ['meteorBrown_big1.png','meteorBrown_big2.png','meteorBrown_med1.png','meteorBrown_med3.png','meteorBrown_small1.png','meteorBrown_small2.png','meteorBrown_tiny1.png']
        self.img_url = img_parent_url + self.img_list[random.randint(0,len(self.img_list) - 1)]
        self.img = pygame.image.load(self.img_url)
        self.rect = self.img.get_rect()
        self.rect.centerx = random.randint(50,750)
        self.rect.top = -100
        self.active = True
        self.speed = 5

    def fly(self):
        if self.active:
            self.rect = self.rect.move(0,self.speed)
        if self.rect.top >= self.window.win_height:
            self.active = False

    def colliderect(self,e):
        if self.active and self.rect.colliderect(e.rect):
            e.kill()

    def update(self):
        self.fly()
        if self.active:
            self.window.window.blit(self.img,self.rect)
