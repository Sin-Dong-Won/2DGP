from pico2d import *

# Boy Event
<<<<<<< HEAD
# fill here
=======
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SLEEP_TIMER, DASH_UP, DASH_DOWN = range(7)
>>>>>>> 0e1161919e5cc36011b5f5a0214632f13224fe0c

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYUP, SDLK_LSHIFT): DASH_UP,
    (SDL_KEYUP, SDLK_RSHIFT): DASH_UP,
    (SDL_KEYDOWN, SDLK_LSHIFT): DASH_DOWN,
    (SDL_KEYDOWN, SDLK_RSHIFT): DASH_DOWN
}



# Boy States
<<<<<<< HEAD
=======
class IdleState:
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1

        boy.timer = 1000

    def exit(boy, event):
        pass

    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer -= 1

        if boy.timer == 0:
            boy.add_event(SLEEP_TIMER)

    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(boy.frame * 100, 300, 100 ,100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 200, 100, 100, boy.x, boy.y)

class RunState:
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1

        boy.dir = boy.velocity

    def exit(boy, event):
        pass
>>>>>>> 0e1161919e5cc36011b5f5a0214632f13224fe0c

# fill here

class DashState:
    def enter(boy, event):
        boy.timer = 50

    def exit(boy, event):
        pass

    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer -= 1
        boy.x += boy.velocity * 2
        boy.x = clamp(25, boy.x,800-25)

        if boy.timer == 0:
            boy.add_event(DASH_UP)

    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(boy.frame * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)


class SleepState:

    def enter(boy, event):
        boy.frame = 0

    def exit(boy, event):
        pass

    def do(boy):
        boy.frame = (boy.frame + 1) % 8

    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_composite_draw(boy.frame * 100, 300, 100, 100, 3.141592 / 2, '', boy.x - 25, boy.y - 25, 100, 100)

        else:
            boy.image.clip_composite_draw(boy.frame * 100, 300, 100, 100, -3.141592 / 2, '', boy.x + 25, boy.y - 25, 100, 100)


next_state_table = {
<<<<<<< HEAD
# fill here
=======
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SLEEP_TIMER: SleepState, DASH_DOWN: IdleState, DASH_UP: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, DASH_UP: RunState,  DASH_DOWN: DashState},
    SleepState: {LEFT_DOWN: RunState, RIGHT_DOWN: RunState, LEFT_UP: RunState, RIGHT_UP: RunState},
    DashState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, DASH_UP: RunState}
>>>>>>> 0e1161919e5cc36011b5f5a0214632f13224fe0c
}







class Boy:

    def __init__(self):
        self.x, self.y = 800 // 2, 90
        self.image = load_image('animation_sheet.png')
        self.dir = 1
        self.velocity = 0
        # fill here
        pass


    def change_state(self,  state):
        # fill here
        pass


    def add_event(self, event):
        # fill here
        pass


    def update(self):
        # fill here
        pass


    def draw(self):
<<<<<<< HEAD
        # fill here
        pass
=======
        self.cur_state.draw(self)
        debug_print('Velocity :' + str(self.velocity) + ' Dir :' + str(self.dir))
>>>>>>> 0e1161919e5cc36011b5f5a0214632f13224fe0c


    def handle_event(self, event):
        # fill here
        pass

