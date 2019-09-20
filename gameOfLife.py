# cellular automata simulation
# By Artur Dorovskikh 2019-09-19

# TODO 2. add array wrapping, 3. then numpy array, 4. parallelization with CYTHON, 

import sys
import pygame as pg
import random
import numpy as np

pg.init()  # initialize pygame
clock = pg.time.Clock() # to calculate fps

# define colors
c_white = (255, 255, 255)
c_black = (0, 0, 0)
c_green = (0, 128, 0)
c_red = (255, 0, 0)

# Set game window resolution
pad = 2
screen_x = screen_y = 400  # TODO fix not being able to set different width and height (array out of bounds)
screen_x_pad, screen_y_pad = screen_x - pad, screen_y - pad
screen = pg.display.set_mode((screen_x ,screen_y))
cells_number = screen_x * screen_y
cells_number_bottom_row = cells_number - screen_x  # for wrapping game world

# cells = np.array([[]]) # TODO try numpy array for possible optimization
# TODO IMPLEMENT ARRAY padding (1 cell border) to avoid using % modulator for better performance
cells = [0 for i in range(cells_number)]  # initialize 1-d array with zeroes
cells_new = cells  # initialize swap array

for i in range(cells_number):
    if random.randint(0, 18) == 1:
        cells[i] = 1

while True:
    # for pygame to be able to stop program
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    screen.fill(c_black)  # TODO-last add past generations fading effect using alpha for pretty effect
    
    # iterate over every cell and compute the next generation
    for y in range(screen_y_pad):  # TODO update for 1-d array, use y*width + x
        for x in range(screen_x_pad):

            y0 = y * screen_y  # up
            y1 = y0 + screen_y  # main
            y2 = y1 + screen_y  #3 down

            x0y0 = x + y0
            x0y1 = x + y1
            x0y2 = x + y2

            cell_count = \
                cells[x0y0] + cells[x0y0 + 1] + cells[x0y0 + 2] + \
                cells[x0y1]                   + cells[x0y1 + 2] + \
                cells[x0y2] + cells[x0y2 + 1] + cells[x0y2 + 2]

            # Conway's Game of Life Rules
            xy = x + 1 + y1
            if cells[xy] == 1:  # check if main cell is alive
                if cell_count < 2 or cell_count > 3:
                    cells_new[xy] = 0
                    pg.draw.line(screen, c_red, (x,y), (x,y)) # draw cell died
                elif cell_count == 3:
                    cells_new[xy] = 1
                    pg.draw.line(screen, c_white, (x,y), (x,y)) # draw cell survived
            elif cell_count == 3:
                cells_new[xy] = 1
                pg.draw.line(screen, c_green, (x,y), (x,y)) # draw cell born
            
    # TODO ### ADD COPYING BEHAVIOR FOR MATRIX WRAPPING
    # top
    # for x in range(screen_x_pad):
    #     cells_new[x] = cells[cells_number_bottom_row + x]
    # # bottom
    # for x in range(screen_x_pad):
    #     cells_new[cells_number_bottom_row + x] = cells[x]

    # left

    # right

    cells = cells_new  # swap cells array to be able to process next generation without conflict

    clock.tick()
    fps = round(clock.get_fps(), 3)
    cells_per_second = round(fps * cells_number)
    pg.display.set_caption(str(fps) + " fps | " + str(cells_per_second) + " cells/s") # show fps
    pg.display.update()
