from constants import *

class Camera:
    # зададим начальный сдвиг камеры и размер поля для возможности реализации циклического сдвига
    def __init__(self, height):
        self.dy = 0
        self.height = height

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.y = self.dy + obj.start_y

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dy = -(target.rect.y + target.rect.h // 2 - HEIGHT // 2)
