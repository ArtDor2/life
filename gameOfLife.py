# Artur Dorovskikh 2019-09-18 added multiprocessing
# Conway's game of life

import sys
import pygame as pg
import random
import numpy as np

pg.init()

#import multiprocessing
# TODO add detect cpu threads in system, set threads to that
# number_of_areas = 4
# area_x = screen_w/processes
# area_y = screen_h/processes

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
cells_x = screen_w - 1  # Used for checking neighbors
cells_y = screen_h - 1  # Used for checking neighbors

cells = [[0 for x in range(screen_w)] for y in range(screen_h)]
cells_new = cells
cells_cleared = [[0 for x in range(screen_w)] for y in range(screen_h)]
# cells = np.array([[]])

#step = 0 # Keeping track of iterations

for x in range(screen_w):
    for y in range(screen_h):
        if random.randint(0, 19) == 1:  # Randomly fill in cells
            cells[x][y] = 1

screen.fill(c_black)
pg.display.update()

clock = pg.time.Clock() # to calculate fps

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    # for i in range(processes):
    #     for process_x in range(number_of_areas): # loop to start process in area horizontal
    #         for process_y in range(number_of_areas): # loop to start process in area vertical
    #             p = multiprocessing.Process(target=compute)
    #             p.start()
    #             p.join() # this line allows you to wait for processes

    screen.fill(c_black)  # TODO add fading effect using alpha
    
    for x in range(screen_w):
        for y in range(screen_h):
            cell_alive = cells[x][y]
            cell_count = cells[x][ (y + 1) % cells_y]               + \
                cells[ (x + 1) % cells_x][y]                   + \
                cells[ (x + 1) % cells_x][(y + 1) % cells_y]   + \
                cells[x][y - 1]                                + \
                cells[x - 1][y]                                + \
                cells[x - 1][y - 1]                            + \
                cells[x - 1][(y + 1) % cells_y]                + \
                cells[ (x + 1) % cells_x][y - 1]

            if cell_alive == 1:
                if cell_count < 2 or cell_count > 3:
                    cells_new[x][y] = 0
                    pg.draw.line(screen, c_red, (x,y), (x,y))
                if cell_count == 3:
                    cells_new[x][y] = 1
                    pg.draw.line(screen, c_white, (x,y), (x,y))
            elif cell_count == 3:
                cells_new[x][y] = 1
                pg.draw.line(screen, c_green, (x,y), (x,y))
            

    cells = cells_new
    cells_new = cells_cleared
    
    #step += 1
    clock.tick()
    pg.display.set_caption(str(clock.get_fps())) # show fps
    pg.display.update()
