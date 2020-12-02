import pygame,sys,random
from module_fj import Window,Hero,Enemy,Brown

# 游戏调节参数设定
hero_shoot_delay = 15
hero_shoot_ready = 0

bullet_speed = 10

enemy_coefficient = 120
enemy_count = 8
enemy_creat_delay = enemy_coefficient/enemy_count
enemy_creat_ready = 0

pygame.init()
window = Window(600,800,'标题',"./img/starfield.png")
hero = Hero('./img/playerShip1_orange.png',window)
enemy_list = []

scope = 0

def showFont(txt,pos,size,window):
    font_name = pygame.font.match_font("华文宋体")
    font = pygame.font.Font(font_name,size)
    fr = font.render(txt,True,(255,255,255))  #得到图层
    txt_rect = fr.get_rect()
    #指定位置
    txt_rect.midtop = pos
    #绘制带文字的图层
    window.blit(fr,txt_rect)

while True:
    # 事件监听
    for e in pygame.event.get():
        # QUIT 退出按钮点击触发状态类型
        if e.type == pygame.QUIT:
            # 系统退出
            sys.exit()
    
    hero.plain()
    hero_shoot_ready += 1
    if hero_shoot_ready >= hero_shoot_delay:
        hero_shoot_ready = 0
        hero.shoot(bullet_speed)

    enemy_creat_ready += 1
    if enemy_creat_ready >= enemy_creat_delay:
        enemy_creat_ready = 0
        if random.randint(0,10) >= 9:
            enemy_list.append(Enemy('./img/p1_jump.png',window))
        else:
            enemy_list.append(Brown('./img/',window))
    
    for i in enemy_list:
        i.fly()
        i.colliderect(hero)
        for j in hero.bullet_list:
            i.colliderect(j)

    window.update()
    hero.update()
    for i in enemy_list:
        i.update()
    
    showFont(str(window.scope),(100,10),50,window.window)
    
    # 窗口更新
    pygame.display.update()
    # 设置刷新率,帧率支持40-200
    clock = pygame.time.Clock()
    clock.tick(60)


