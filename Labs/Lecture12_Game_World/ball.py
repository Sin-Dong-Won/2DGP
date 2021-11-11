from pico2d import *
import game_world

class Ball:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.velocity

        if self.x < 25 or self.x > 1600 - 25:
<<<<<<< HEAD
            game_world.remove_object(self)
=======
            game_world.remove_object(self) # 축구공이 맵 밖을 벗어났으므로 제거한다.
>>>>>>> 0e1161919e5cc36011b5f5a0214632f13224fe0c
