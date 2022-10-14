import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")

    # 创建一艘ship
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储alien的编组
    aliens = Group()
    # 创建一个用于存储bullet的编组
    bullets = Group()

    # 创建 alien 群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)

        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(aliens)

        # 每次循环时都重绘屏幕
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
