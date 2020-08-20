from random import randint
from time import sleep


def clamp(minn, maxx, value):
    return sorted([minn, maxx, value])[1]


def generate_terrain(main_func_list):
    if len(main_func_list) < 20:
        main_func_list.append(0)
        print("reset")
        while len(main_func_list) < 20:
            main_func_list.append(clamp(-6, 6, main_func_list[0] + randint(-1, 1)))
    else:
        del main_func_list[len(main_func_list)-1]
        shift_terrain = clamp(-6, 6, main_func_list[0] + randint(-1, 1))
        main_func_list.insert(0, shift_terrain)
    return main_func_list


def draw_line(pl_x, shift):
    terrain = list(f"{'#' * (6 - shift)}{' ' * 8}{'#' * (6 + shift)}")
    terrain.insert(0, "||")
    terrain.insert(41, "||")
    terrain[pl_x] = 'o'
    return ''.join(terrain)


shift_num = 0
terrain_list = []
terrain_list = generate_terrain(terrain_list)
for i in terrain_list:
    print(draw_line(-terrain_list[0]+10, terrain_list[0]))
for x in range(100):
    terrain_list = generate_terrain(terrain_list)
    sleep(.3)
    print(draw_line(-terrain_list[0]+10, terrain_list[0]))

