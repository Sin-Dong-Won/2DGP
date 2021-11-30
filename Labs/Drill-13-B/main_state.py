import random
import json
import os

from pico2d import *
import game_framework
import game_world
import server
from boy import Boy
from grass import Grass
from ball import Ball
from brick import Brick

name = "MainState"

before_collide = None

def collide(a, b):
    # fill here
    global before_collide

    before_collide = b
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def enter():
    server.boy = Boy()
    game_world.add_object(server.boy, 1)

    server.grass = Grass()
    game_world.add_object(server.grass, 0)


    server.bricks = [Brick(300 + 300 * i, 100 + 50 * i) for i in range(5)]
    game_world.add_objects(server.bricks, 1)


def exit():
    game_world.clear()


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            server.boy.handle_event(event)


def update():
    global before_collide

    for game_object in game_world.all_objects():
        game_object.update()

    for ball in server.balls.copy():
        if collide(ball, server.grass):
            ball.stop()
        if collide(ball, server.boy):
            server.balls.remove(ball)
            game_world.remove_object(ball)






def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
