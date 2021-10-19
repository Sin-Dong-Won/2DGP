from pico2d import *
import random

class small_ball:
    def __init__(self):
        self.x = random.randint(0, 200)
        self.y = 599
        self.speed = random.randint(0, 10)
        self.image = small_ball1

    def fall(self):
        self.y = self.y - self.speed

    def draw(self):
        self.image.draw(self.x, self.y)


class big_ball:
    def __init__(self):
        self.x = random.randint(0, 200)
        self.y = 599
        self.speed = random.randint(0, 10)
        self.image = big_ball1

    def fall(self):
        self.y = self.y - self.speed

    def draw(self):
        self.image.draw(self.x, self.y)

open_canvas()

small_ball1 = load_image('ball21x21.png')
big_ball1 = load_image('ball41x41.png')
grass = load_image('grass.png')

small_balls = [small_ball() for i in range(10)]
big_balls = [big_ball() for j in range(10)]

running = True

while running:
    clear_canvas()
    grass.draw(400, 90)
    update_canvas()





update_canvas()
