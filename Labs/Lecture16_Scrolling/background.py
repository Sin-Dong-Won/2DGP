import random
import server

from pico2d import *


class TileBackground:

    def __init__(self):
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = 800 * 3
        self.h = 600 * 3

        # fill
        self.tiles = [[load_image('cube%d%d.png' % (x, y)) for x in range(3)] for y in range(3)]

    def update(self):
        pass

    def draw(self):
        self.window_left = clamp(0,
                                 int(server.boy.x) - self.canvas_width // 2,
                                 self.w - self.canvas_width)
        self.window_bottom = clamp(0,
                                   int(server.boy.y) - self.canvas_height // 2,
                                   self.h - self.canvas_height)

        tile_left = self.window_left // 800
        tile_right = min((self.window_left + self.canvas_width) // 800 + 1, 3)
        left_offset = self.window_left % 800

        tile_bottom = self.window_bottom // 600
        tile_top = min((self.window_bottom + self.canvas_height) // 600 + 1, 3)
        bottom_offset = self.window_bottom % 600

        for ty in range(tile_bottom, tile_top):
            for tx in range(tile_left, tile_right):
                self.tiles[ty][tx].draw_to_origin(-left_offset + (tx - tile_left) * 800, -bottom_offset + (ty - tile_bottom) * 600)


class FixedBackground:

    def __init__(self):
        self.image = load_image('futsal_court.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h

    def draw(self):
        self.image.clip_draw_to_origin(self.window_left, self.window_bottom, server.background.canvas_width, server.background.canvas_height, 0, 0)

    def update(self):
        self.window_left = clamp(0, int(server.boy.x) - server.background.canvas_width // 2, server.background.w - server.background.canvas_width)
        self.window_bottom = clamp(0, int(server.boy.y) - server.background.canvas_height // 2, server.background.h - server.background.canvas_height)

    def handle_event(self, event):
        pass


class InfiniteBackground:

    def __init__(self):
        self.image = load_image('futsal_court.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h

    def draw(self):
        self.image.clip_draw_to_origin(self.q3l, self.q3b, self.q3w, self.q3h, 0, 0)  # quadrant 3
        self.image.clip_draw_to_origin(self.q2l, self.q2b, self.q2w, self.q2h, 0, self.q3h)  # quadrant 2
        self.image.clip_draw_to_origin(self.q4l, self.q4b, self.q4w, self.q4h, self.q3w, 0)  # quadrant 4
        self.image.clip_draw_to_origin(self.q1l, self.q1b, self.q1w, self.q1h, self.q3w, self.q3h)  # quadrant 1

    def update(self):
        # quadrant 3
        self.q3l = (int(server.boy.x) - self.canvas_width // 2) % self.w
        self.q3b = (int(server.boy.y) - self.canvas_height // 2) % self.h
        self.q3w = clamp(0, self.w - self.q3l, self.w)
        self.q3h = clamp(0, self.h - self.q3b, self.h)
        # quadrant 2
        self.q2l = self.q3l
        self.q2b = 0
        self.q2w = self.q3w
        self.q2h = self.canvas_height - self.q3h
        # quadrand 4
        self.q4l = 0
        self.q4b = self.q3b
        self.q4w = self.canvas_width - self.q3w
        self.q4h = self.q3h
        # quadrand 1
        self.q1l = 0
        self.q1b = 0
        self.q1w = self.q4w
        self.q1h = self.q2h

    def handle_event(self, event):
        pass
