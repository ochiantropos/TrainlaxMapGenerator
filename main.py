




# --------------------------------------------------------------------------------- #

# libraries requird
import pygame
import random
from pprint import pprint

from grid import Grid
from tile import Tile

wh = 9
hx = 15

end_point = []
start_point = []

second_start_point = [None, None]
second_end_point = [None, None]

is_number_of_start_end = False
number_of_start_end = 1
is_point = False

print("Start-End point count >>: ")
while True:
    try:
        set_wh = input()
        if set_wh != "":
            number_of_start_end = int(set_wh)
            is_number_of_start_end = True
            is_point = True
            break

        else:
            break

    except:
        print("\n\n!!! input not valid\n\n")
        continue


pprint(is_number_of_start_end)
    
def donot_valid_position(arr: list):
    if arr[0] == 0 and arr[1] == 0:
        return True
    elif arr[0] == 0 and arr[1] == hx-1:
        return True
    elif arr[0] == wh-1 and arr[1] == hx-1:
        return True
    elif arr[0] == wh-1 and arr[1] == 0:
        return True
    else:
        return False


types = []

variants = [
    [[wh - 1,  3     ], 1, 20],
    [[wh - 1,  hx//2 ], 2, 21],
    [[wh - 1,  hx-4  ], 3, 20],

    [[0,       hx-4  ], 4, 20],
    [[0,       hx//2 ], 5, 21],
    [[0,       3     ], 6, 20],

    [[wh - 3,  0     ], 7, 21],
    [[wh // 2, 0     ], 8, 20],
    [[2,       0     ], 9, 21],

    [[2,       hx-1  ], 10, 21],
    [[wh // 2, hx-1  ], 11, 20],
    [[wh-3,    hx-1  ], 12, 21],
]

start_point = random.choice(variants)

end_point = random.choice(variants)
while start_point[1] == end_point[1]:
    end_point = random.choice(variants)


if is_number_of_start_end:
    second_start_point = random.choice(variants)
    while start_point[1] == second_start_point[1] or end_point[1] == second_start_point[1]:
        second_start_point = random.choice(variants)

    second_end_point = random.choice(variants)
    while start_point[1] == second_end_point[1] or end_point[1] == second_end_point[1] or second_end_point[1] == second_start_point[1]:
        second_end_point = random.choice(variants)

types.append(start_point[-1])
types.append(end_point[-1])

start_point = start_point[0]
end_point = end_point[0]

if is_number_of_start_end:
    types.append(second_start_point[-1])
    types.append(second_end_point[-1])

    second_start_point = second_start_point[0]
    second_end_point = second_end_point[0]
#
# if not is_point:
#     start_point = rundom_border_point()
#     while donot_valid_position(start_point):
#         start_point = rundom_border_point()
#
#
#     end_point = rundom_border_point()
#     while start_point[0] != end_point[0] and start_point[1] != end_point[1] and donot_valid_position(end_point):
#         end_point = rundom_border_point()

with open("start_end_points_temp.txt", 'w') as point_temp:
    pass


pygame.init()

# initializong the font object
font = pygame.font.Font("./assets/custom_fonts/Poppins/Poppins-Light.ttf", 16)

# --------------------------------------------------------------------------------- #

# global variables
rez = 30
width = wh * rez
height = hx * rez
display = pygame.display.set_mode((height, width))

# --------------------------------------------------------------------------------- #
# function for loading images with given resolution/size
def load_image(path, rez_, padding = 0):
    img = pygame.image.load(path).convert_alpha()
    img = pygame.transform.scale(img, (rez_ - padding, rez_ - padding))
    return img

# --------------------------------------------------------------------------------- #

# function for displayong a given message
def disp_msg(text, x, y):
    msg = font.render(str(text), 1, (255, 255, 255))
    display.blit(msg, (x, y))

# --------------------------------------------------------------------------------- #

# debug tool 
# when mouse is hovered over a cell, if displays the 
#       [ ] cell entropy
#       [ ] cell collapsed boolean
#       [ ] cell options / tiles
def hover(mouse_pos, rez, grid):
    mx, my = mouse_pos
    x = mx // rez
    y = my // rez
    cell = grid.grid[y][x]

    # cell information
    cell_entropy = cell.entropy()
    cell_collpased = cell.collapsed
    cell_options = [opt.edges for opt in cell.options]

    # hover box
    pygame.draw.rect(display, (20, 20, 20), (mouse_pos[0], mouse_pos[1], 200, 100))

    # hover text/info
    disp_msg(f"entrophy  : {cell_entropy}", mx + 10, my + 10)
    disp_msg(f"collapsed : {cell_collpased}", mx + 10, my + 30)
    disp_msg(f"options   : {cell_options}", mx + 10, my + 50)

# --------------------------------------------------------------------------------- #

# main game function
def main():
    #clear temp
    
    with open("temp.txt", "w") as f:
        pass
    
    
    # loading tile images
    options = []
    for i in range(16):
        # load tetris tile
        # img = load_image(f"./assets/{i}.png", rez)
        # load corner tile
        img = load_image(f"./assets/c{i}.png", rez)
        options.append(Tile(img))

    # edge conditions for tetris tiles
    # options[0].edges = [0, 0, 0, 0]
    # options[1].edges = [1, 1, 0, 1]
    # options[2].edges = [1, 1, 1, 0]
    # options[3].edges = [0, 1, 1, 1]
    # options[4].edges = [1, 0, 1, 1]

    # edge conditions for corner tiles
    options[0].edges = [0, 0, 0, 0]
    options[1].edges = [1, 1, 0, 0]
    options[2].edges = [0, 1, 1, 0]
    options[3].edges = [0, 0, 1, 1]
    options[4].edges = [1, 0, 0, 1]
    
    options[5].edges = [1, 0, 1, 1]
    options[6].edges = [0, 1, 1, 1]
    options[7].edges = [1, 1, 1, 0]
    options[8].edges = [1, 1, 0, 1]
    
    options[9].edges = [1, 0, 1, 1]
    options[10].edges = [0, 1, 1, 1]
    options[11].edges = [1, 1, 1, 0]
    options[12].edges = [1, 1, 0, 1]
    
    options[13].edges = [1, 1, 1, 1]
    
    options[14].edges = [1, 0, 1, 0]
    options[15].edges = [0, 1, 0, 1]
    
    

    # update tile rules for each tile
    for i, tile in enumerate(options):
        tile.index = i 
        tile.set_rules(options)

    # wave grid
    wave = Grid(width, height, rez, options)
    wave.initiate()

    pprint(start_point)
    pprint(end_point)
    pprint(second_start_point)
    pprint(second_end_point)

    wave.collapse_all_border_cell(start_point, end_point, second_start_point, second_end_point, is_number_of_start_end, types)
    # toggle for displaying debug information
    hover_toggle = False

    # game loop
    loop = True
    
    
    while loop:

        display.fill((0, 0, 0))
        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                wave.WriteAll();

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    hover_toggle = not hover_toggle
                    wave.WriteAll();
                    

                if event.key == pygame.K_q:
                    loop = False
                    wave.WriteAll();
                    exit()
            
        # grid draw function
        wave.draw(display)
        # grid collapse method to run the alogorithm
        wave.collapse()

        # mouse position and hover debug
        if hover_toggle:
            mos_pos = pygame.mouse.get_pos()
            hover(mos_pos, rez, wave)

        # update the display
        pygame.display.flip()

# --------------------------------------------------------------------------------- #

# calling the main function
if __name__ == "__main__":
    main()

# --------------------------------------------------------------------------------- #
