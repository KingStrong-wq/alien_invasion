import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个 alien 的类"""

    def __init__(self, ai_settings, screen):
        """初始化 alien 并设置其起始位置"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载alien图像，并设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个 alien 最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储 alien 的准确位置
        self.x = float(self.rect.x)

    def update(self):
        """向右移动alien"""
        self.x += self.ai_settings.alien_speed_factor
        self.rect.x = self.x

    def blitme(self):
        """在指定位置绘制 alien"""
        self.screen.blit(self.image, self.rect)
