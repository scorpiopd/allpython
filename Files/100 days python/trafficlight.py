from time import sleep
import itertools
import random

colors="red Green Amber".split()
rotation=itertools.cycle(colors)

def rg_timer():
    return random.randint(3,7)

def light_rotation(rotation):
    for color in rotation:
        if color == 'Amber':
            print(f"caution light is {color}")
            sleep(3)

        elif color == "Red":
            print(f"stop now light is {color}")
            sleep(rg_timer())
        else:
            print(f"light is {color}")
            sleep(rg_timer())



if __name__ == '__main__':
    light_rotation(rotation)