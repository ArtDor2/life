# Artur Dorovskikh 2019-09-18 added multiprocessing
# Conway's game of life

import sys
import pygame as pg
import random

#import multiprocessing
# processes = 16 # needs to be even number
# number_of_areas = 4
# area_x = screen_w/processes
# area_y = screen_h/processes

pg.init()

# Set window resolution
screen_w = screen_h = 400
screen = pg.display.set_mode((screen_w,screen_h))

# Set the colors
c_white = (255, 255, 255)
c_black = (0, 0, 0)
c_green = (0, 128, 0)
c_red = (255, 0, 0)
c_yellow = (255, 255, 0)

# Set cells and array
cells_x_l = screen_w  # Used in for loops, because a list starts with 0 then 1
cells_y_l = screen_h  # Used in for loops, because a list starts with 0 then 1
cells_x = cells_x_l - 1  # Used for checking neighbors
cells_y = cells_y_l - 1  # Used for checking neighbors
cells = [[0 for x in range(cells_x_l)] for y in range(cells_y_l)]
cells_new = cells
step = 0 # Keeping track of iterations

for x in range(cells_x_l):
    for y in range(cells_y_l):
        if random.randint(0, 19) == 1:  # Randomly fill in cells
            cells[x][y] = 1

screen.fill(c_black)
pg.display.update()


# Count cell nearest neighbors
def count_cells(x, y): # x_cell, y_cell, radius):
    ## weird pattern:
    
    return  cells[x][ (y + 1) % cells_y]               + \
        cells[ (x + 1) % cells_x][y]                   + \
        cells[ (x + 1) % cells_x][(y + 1) % cells_y]   + \
        cells[x][y - 1]                                + \
        cells[x - 1][y]                                + \
        cells[x - 1][y - 1]                            + \
        cells[x - 1][(y + 1) % cells_y]                + \
        cells[ (x + 1) % cells_x][y - 1]


def draw_pixel(pixel_color, pixel_x, pixel_y):
    pg.draw.line(screen, pixel_color, (pixel_x,pixel_y), (pixel_x,pixel_y)) # 4.3 fps
    #pg.draw.circle(screen, pixel_color, (pixel_x,pixel_y), 1) # 4fps
    #return # drawing nothing is 4 fps

clock = pg.time.Clock() # to calculate fps

def compute(x, y):
    cell_alive = cells[x][y]
    cell_count = count_cells(x, y)

    if cell_alive == 1:
        if cell_count < 2 or cell_count > 3:
            cells_new[x][y] = 0
            draw_pixel(c_red, x, y)
    elif cell_count == 3:
            cells_new[x][y] = 1
            # draw_pixel(c_green, x, y)
            draw_pixel(c_white, x, y)

    # if cell_alive and cells_new[x][y] == 1:
    #     draw_pixel(c_white, x, y)


while True:
    # for i in range(processes):
    #     for process_x in range(number_of_areas): # loop to start process in area horizontal
    #         for process_y in range(number_of_areas): # loop to start process in area vertical
    #             p = multiprocessing.Process(target=compute)
    #             p.start()
    #             p.join() # this line allows you to wait for processes

    screen.fill(c_black)
    
    # these loops (even without neighbor counting) drop fps from 1500 (without these loops) to 17
    for x in range(cells_x_l):
        for y in range(cells_y_l):
            compute(x, y)
            

    cells, cells_new = cells_new, cells
    #cells_new = [[0 for x in range(cells_x_l)] for y in range(cells_y_l)]
    #step += 1

    clock.tick()
    pg.display.set_caption(str(clock.get_fps())) # str(step) + 
    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
