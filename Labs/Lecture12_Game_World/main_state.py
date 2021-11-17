import random
import json
import os

from pico2d import *
import game_framework
import game_world


from boy import Boy

from boy_ball import Boy

from grass import Grass
from ball import Ball


name = "MainState"

boy = None
grass = None

def enter():
    global boy, grass
    boy = Boy()
    grass = Grass()

    game_world.add_object(grass, 0) # 게임 월드에 잔디 객체 추가?
    game_world.add_object(boy, 1) # 게임 월드에 소년 객체 추가?



def exit():
    global boy, grass
    del boy
    del grass

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
            boy.handle_event(event)


def update():

    boy.update()

    for game_object in game_world.all_objects(): # 게임 월드 내의 모든 오브젝트를 하나씩 꺼내서
        game_object.update() # 업데이트 한다.



def draw():
    clear_canvas()
    grass.draw()
    boy.draw()

    for game_object in game_world.all_objects(): # 게임 월드 내의 모든 오브젝트를 하나씩 꺼내서
        game_object.draw() # 그린다.

    update_canvas()







