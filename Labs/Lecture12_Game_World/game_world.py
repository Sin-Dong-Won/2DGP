
# layer 0: Background Objects
# layer 1: Foreground Objects
objects = [[],[]]


def add_object(o, layer):
    objects[layer].append(o)


def add_objects(l, layer):
    objects[layer] += l


def remove_object(o):
    for i in range(len(objects)):
        if o in objects[i]:
            objects[i].remove(o)
            del o
            break

<<<<<<< HEAD



=======
>>>>>>> 0e1161919e5cc36011b5f5a0214632f13224fe0c
def clear():
    for o in all_objects():
        del o
    for l in objects:
        l.clear()

<<<<<<< HEAD
=======

>>>>>>> 0e1161919e5cc36011b5f5a0214632f13224fe0c
def destroy():
    clear()
    objects.clear()


def all_objects():
    for i in range(len(objects)):
        for o in objects[i]:
            yield o

