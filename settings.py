class Settings:
    """存储game的所有设置的类"""

    def __init__(self):
        """初始化game setting"""
        # 屏幕设置
        self.screen_width = 600
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_speed_factor = 0.1

        # 子弹设置
        self.bullet_speed_factor = 0.4
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # alien 设置
        self.alien_speed_factor = 1
