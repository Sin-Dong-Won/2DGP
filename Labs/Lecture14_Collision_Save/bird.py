import game_framework
from pico2d import *
import random

import game_world

# Bird Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
BIRD_SPEED_KMPH = 1.0  # Km / Hour
BIRD_SPEED_MPM = (BIRD_SPEED_KMPH * 1000.0 / 60.0)
BIRD_SPEED_MPS = (BIRD_SPEED_MPM / 60.0)
BIRD_SPEED_PPS = (BIRD_SPEED_MPS * PIXEL_PER_METER)

# Bird Action Speed
TIME_PER_ACTION = 2
ACTION_PER_TIME = 10.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 1


class Bird:
    def __init__(self):
        self.x = random.randint(600, 800 + 1)
        self.y = random.randint(50, 250 + 1)
        self.dir = random.randint(0, 1 + 1)
        self.velocity = BIRD_SPEED_PPS

        self.frame = 0
        self.image = load_image('bird100x100x14.png')
        self.reverse_image = load_image('bird100x100x14_reverse.png')
        self.cur = 0

    def update(self):
        if self.dir == 0:
            self.dir = -1

        if self.dir == 1:
            self.x += self.velocity
            self.cur = self.image
        else:
            self.x -= self.velocity
            self.cur = self.reverse_image

        self.frame = (self.frame + TIME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14

        if self.x <= 0:
            self.dir = 1
        elif self.x >= 1600:
            self.dir = -1

    def draw(self):
        self.cur.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y)


