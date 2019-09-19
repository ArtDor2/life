# Artur Dorovskikh 2019-09-18 added multiprocessing
# Conway's game of life

import sys
import pygame as pg
import random
import numpy as np
import multiprocessing

pg.init()  # initialize pygame

# Set game window resolution
screen_x = screen_y = 400  # TODO fix not being able to set different width and height
screen = pg.display.set_mode((screen_x,screen_y))
number_of_cells = screen_x * screen_y
clock = pg.time.Clock() # to calculate fps

# Set the colors
c_white = (255, 255, 255)
c_black = (0, 0, 0)
c_green = (0, 128, 0)
c_red = (255, 0, 0)
# c_yellow = (255, 255, 0)

# Set cell boundaries
cell_x = screen_x - 1  # -1 to avoid out of bounds error in array
cell_y = screen_y - 1  # -1 to avoid out of bounds error in array

# TODO IMPLEMENT ARRAY WRAPPING (1 cell border) to avoid using % modulator for better performance
# cells = [[0 for x in range(screen_x)] for y in range(screen_y)]  # for array wrapping
cells = [[0 for x in range(screen_x)] for y in range(screen_y)]  # no array wrapping
cells_new = cells
# cells = np.array([[]]) # TODO try numpy array for possible optimization

# Randomly fill in cells into world
for x in range(screen_x):
    for y in range(screen_y):
        if random.randint(0, 18) == 1:
            cells[x][y] = 1

# # for multithreaded:
# def compute_next_cells(cells_range_x, cells_range_y):
#     for x in range(cells_range_x):
#         for y in range(cells_range_y):
#             # TODO fix wrong counting (generates cool rug patterns)
#             # count surrounding 8 cell neighbors
#             cell_count = cells[x][ (y + 1) % cell_y]          + \
#                 cells[ (x + 1) % cell_x][y]                   + \
#                 cells[ (x + 1) % cell_x][(y + 1) % cell_y]    + \
#                 cells[x][y - 1]                               + \
#                 cells[x - 1][y]                               + \
#                 cells[x - 1][y - 1]                           + \
#                 cells[x - 1][(y + 1) % cell_y]                + \
#                 cells[ (x + 1) % cell_x][y - 1]

#             # Conway's Game of Life Rules
#             if cells[x][y] == 1:  # check if main cell is alive
#                 if cell_count < 2 or cell_count > 3:
#                     cells_new[x][y] = 0
#                     pg.draw.line(screen, c_red, (x,y), (x,y)) # draw cell died
#                 if cell_count == 3:
#                     cells_new[x][y] = 1
#                     pg.draw.line(screen, c_white, (x,y), (x,y)) # draw cell survived
#             elif cell_count == 3:
#                 cells_new[x][y] = 1
#                 pg.draw.line(screen, c_green, (x,y), (x,y)) # draw cell born

# # MULTITHREADED loop # TODO implement multithreading
# cpu_count = multiprocessing.cpu_count()
# area_step_size = screen_x/cpu_count  # how many cells per cell area

# for area_step_num in cpu_count:  # launch a process per cell area
#     p = multiprocessing.Process(target=compute_next_cells(area_step_num*area_step_size, 0))
#     p.start()
#     p.join() # this line allows you to wait for processes

# SINGLETHREADED loop
while True:
    # for pygame to be able to exit
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    screen.fill(c_black)  # TODO-last add fading effect using alpha
    
    # iterate over every cell and compute the next generation
    for x in range(screen_x):
        for y in range(screen_y):
            # TODO fix wrong counting (generates weird patterns)
            # TODO use array wrappig (1 cell border) to avoid using % modulator for better performance
            # count surrounding 8 cell neighbors
            cell_count = cells[x][ (y + 1) % cell_y]          + \
                cells[ (x + 1) % cell_x][y]                   + \
                cells[ (x + 1) % cell_x][(y + 1) % cell_y]    + \
                cells[x][y - 1]                               + \
                cells[x - 1][y]                               + \
                cells[x - 1][y - 1]                           + \
                cells[x - 1][(y + 1) % cell_y]                + \
                cells[ (x + 1) % cell_x][y - 1]

            # Conway's Game of Life Rules
            if cells[x][y] == 1:  # check if main cell is alive
                if cell_count < 2 or cell_count > 3:
                    cells_new[x][y] = 0
                    pg.draw.line(screen, c_red, (x,y), (x,y)) # draw cell died
                if cell_count == 3:
                    cells_new[x][y] = 1
                    pg.draw.line(screen, c_white, (x,y), (x,y)) # draw cell survived
            elif cell_count == 3:
                cells_new[x][y] = 1
                pg.draw.line(screen, c_green, (x,y), (x,y)) # draw cell born
            
    cells = cells_new  # swap cells array to be able to process next generation without conflict
    
    clock.tick()
    fps = round(clock.get_fps(), 3)
    cells_per_second = round(fps * number_of_cells)
    pg.display.set_caption(str(fps) + " fps | " + str(cells_per_second) + " cells/s") # show fps
    pg.display.update()
