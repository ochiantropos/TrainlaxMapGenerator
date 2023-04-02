
# --------------------------------------------------------------------------------- #
# required libraries
import copy
import random
from cell import Cell
from pprint import pprint
# --------------------------------------------------------------------------------- #

# Grid class
class Grid:
    types = []


    def __init__(self, width, height, rez, options):
        self.width = width
        self.height = height
        self.rez = rez
        self.w = self.width // self.rez
        self.h = self.height // self.rez
        self.grid = []
        self.options = options

    # initiate each spot in the grid with a cell object
    def initiate(self):
        for i in range(self.w):
            self.grid.append([])
            for j in range(self.h):
                cell = Cell(i, j, self.rez, self.options)
                self.grid[i].append(cell)

    # draw each cell in the grid
    def draw(self, win):
        for row in self.grid:
            for cell in row:
                cell.draw(win)

    def collapse_all_border_cell(self, inp: list, out: list, second_inp: list, second_out: list, is_second: bool, types: list):
        inp_type = None
        out_type = None
        second_inp_type = None
        second_out_type = None

        if inp[0] == 0 or inp[0] == self.w-1:
            self.grid[inp[0]][inp[1]].options
            self.grid[inp[0]][inp[1]].do_14()
            inp_type = 14
            
        else:
            self.grid[inp[0]][inp[1]].options
            self.grid[inp[0]][inp[1]].do_15()
            inp_type = 15

            
        if out[0] == 0 or out[0] == self.w-1:
            self.grid[out[0]][out[1]].options
            self.grid[out[0]][out[1]].do_14()
            out_type = 14

        else:
            self.grid[out[0]][out[1]].options
            self.grid[out[0]][out[1]].do_15()
            out_type = 15

        if is_second:
            if second_inp[0] == 0 or second_inp[0] == self.w - 1:
                self.grid[second_inp[0]][second_inp[1]].options
                self.grid[second_inp[0]][second_inp[1]].do_14()
                second_inp_type = 14
            else:
                self.grid[second_inp[0]][second_inp[1]].options
                self.grid[second_inp[0]][second_inp[1]].do_15()
                second_inp_type = 15

            if second_out[0] == 0 or second_out[0] == self.w - 1:
                self.grid[second_out[0]][second_out[1]].options
                self.grid[second_out[0]][second_out[1]].do_14()
                second_out_type = 14
            else:
                self.grid[second_out[0]][second_out[1]].options
                self.grid[second_out[0]][second_out[1]].do_15()
                second_out_type = 15

        for i in range(self.w):
            self.grid[i][self.h-1].options
            self.grid[i][self.h-1].do_zero()
            self.grid[i][0].options
            self.grid[i][0].do_zero()

        for i in range(self.h):
            self.grid[0][i].options
            self.grid[0][i].do_zero()
                
            self.grid[self.w-1][i].options
            self.grid[self.w-1][i].do_zero()
            
        with open("start_end_points_temp.txt", 'w') as point_temp:
            if inp_type == 14 and types[0] == 20:
                point_temp.write(f"[20,{inp[0]*4},0,{inp[1]*4}]\n")
                self.types.append(["20", inp])

            elif inp_type == 14 and types[0] == 21:
                point_temp.write(f"[21,{inp[0]*4},0,{inp[1]*4}]\n")
                self.types.append(["21", inp])


            elif inp_type == 15 and types[0] == 20:
                point_temp.write(f"[22,{inp[0]*4},0,{inp[1]*4}]\n")
                self.types.append(["22", inp])


            elif inp_type == 15 and types[0] == 21:
                point_temp.write(f"[23,{inp[0]*4},0,{inp[1]*4}]\n")
                self.types.append(["23", inp])

            if out_type == 14 and types[1] == 20:
                point_temp.write(f"[20,{out[0] * 4},0,{out[1] * 4}]")
                self.types.append(["20", out])


            elif out_type == 14 and types[1] == 21:
                point_temp.write(f"[21,{out[0] * 4},0,{out[1] * 4}]")
                self.types.append(["21", out])


            elif out_type == 15 and types[1] == 20:
                point_temp.write(f"[22,{out[0] * 4},0,{out[1] * 4}]")
                self.types.append(["22", out])


            elif out_type == 15 and types[1] == 21:
                point_temp.write(f"[23,{out[0] * 4},0,{out[1] * 4}]")
                self.types.append(["23", out])


            if is_second:
                if second_inp_type == 14 and types[2] == 20:
                    point_temp.write(f"\n[20,{second_inp[0] * 4},0,{second_inp[1] * 4}]\n")
                    self.types.append(["20", second_inp])

                elif second_inp_type == 14 and types[2] == 21:
                    point_temp.write(f"\n[21,{second_inp[0] * 4},0,{second_inp[1] * 4}]\n")
                    self.types.append(["21", second_inp])

                elif second_inp_type == 15 and types[2] == 20:
                    point_temp.write(f"\n[22,{second_inp[0] * 4},0,{second_inp[1] * 4}]\n")
                    self.types.append(["22", second_inp])

                elif second_inp_type == 15 and types[2] == 21:
                    point_temp.write(f"\n[23,{second_inp[0] * 4},0,{second_inp[1] * 4}]\n")
                    self.types.append(["23", second_inp])

                if second_out_type == 14 and types[3] == 20:
                    point_temp.write(f"[20,{second_out[0] * 4},0,{second_out[1] * 4}]")
                    self.types.append(["20", second_out])

                elif second_out_type == 14 and types[3] == 21:
                    point_temp.write(f"[21,{second_out[0] * 4},0,{second_out[1] * 4}]")
                    self.types.append(["20", second_out])

                elif second_out_type == 15 and types[3] == 20:
                    point_temp.write(f"[22,{second_out[0] * 4},0,{second_out[1] * 4}]")
                    self.types.append(["22", second_out])

                elif second_out_type == 15 and types[3] == 21:
                    point_temp.write(f"[23,{second_out[0] * 4},0,{second_out[1] * 4}]")
                    self.types.append(["23", second_out])
        print(self.types)


    def _is_in_type_s(self, cell):
        for item in self.types:
            if cell.x == item[1][0] and cell.y == item[1][1]:
                return True, item[0]
            else:
                continue
        return False, ""

    def WriteAll(self):
        for row in self.grid:
            for cell in row:  
                if cell.options[0].index != 0:
                    pprint(f"Colapse: str: ({cell.x},{cell.y}) type = {cell.options[0].index}")
                    res, index = self._is_in_type_s(cell)
                    pprint(f"cell : {res} {index} {cell.x},{cell.y}")
                    with open("temp.txt", "a") as temp:
                        if res:
                            temp.write(f"[{index},{cell.x*4},0,{cell.y*4}]\n")
                        else:
                            temp.write(f"[{cell.options[0].index},{cell.x*4},0,{cell.y*4}]\n")

    def heuristic_pick(self): # randomly pick a cell using [entropy heuristic]

        # shallow copy of a grid
        grid_copy = [i for row in self.grid for i in row]
        grid_copy.sort(key=lambda x: x.entropy())

        filtered_grid = list(filter(lambda x: x.entropy() > 1, grid_copy))

        if filtered_grid == []:
            return None

        initial = filtered_grid[0]
        filtered_grid = list(filter(lambda x: x.entropy() == initial.entropy(), filtered_grid))

        # return a pick if filtered copy os not empty
        pick = random.choice(filtered_grid)
        return pick

    # [WAVE FUNCTION COLLAPSE] algorithm
    def collapse(self):

        # pick a random cell using entropy heuristic
        pick = self.heuristic_pick()
        if pick:
            self.grid[pick.x][pick.y].options
            self.grid[pick.x][pick.y].observe()
        else:
            return

        # shallow copy of the gris
        next_grid = copy.copy(self.grid)

        # update the entropy values and superpositions of each cell in the grid
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j].collapsed:
                    next_grid[i][j] = self.grid[i][j]

                else:
                    # cumulative_valid_options will hold the options that will satisfy the "down", "right", "up", "left" 
                    # conditions of each cell in the grid. The cumulative_valid_options is computed by,

                    cumulative_valid_options = self.options
                    # check above cell
                    cell_above = self.grid[(i - 1) % self.w][j]
                    valid_options = []                          # holds the valid options for the current cell to fit with the above cell
                    for option in cell_above.options:
                        valid_options.extend(option.down)
                    cumulative_valid_options = [option for option in cumulative_valid_options if option in valid_options]

                    # check right cell
                    cell_right = self.grid[i][(j + 1) % self.h]
                    valid_options = []                          # holds the valid options for the current cell to fit with the right cell
                    for option in cell_right.options:
                        valid_options.extend(option.left)
                    cumulative_valid_options = [option for option in cumulative_valid_options if option in valid_options]

                    # check down cell
                    cell_down = self.grid[(i + 1) % self.w][j]
                    valid_options = []                          # holds the valid options for the current cell to fit with the down cell
                    for option in cell_down.options:
                        valid_options.extend(option.up)
                    cumulative_valid_options = [option for option in cumulative_valid_options if option in valid_options]

                    # check left cell
                    cell_left = self.grid[i][(j - 1) % self.h]
                    valid_options = []                          # holds the valid options for the current cell to fit with the left cell
                    for option in cell_left.options:
                        valid_options.extend(option.right)
                    cumulative_valid_options = [option for option in cumulative_valid_options if option in valid_options]

                    # finally assign the cumulative_valid_options options to be the current cells valid options
                    next_grid[i][j].options = cumulative_valid_options
                    next_grid[i][j].update()

        # re-assign the grid value after cell evaluation
        self.grid = copy.copy(next_grid)
