# Artur Dorovskikh 2017 Jan 27-28, Feb 4
# My first medium size project in python and in programming

import sys, pygame as pg, random
pg.init()

# Set window resolution
screen_w = 600
screen_h = 600
screen = pg.display.set_mode((screen_w,screen_h))

# Set the colors
c_white = (255, 255, 255)
c_black = (0, 0, 0)

# Set cells and array
cell_s = 3
cell_s_h = int(cell_s/2)
cells_x_l = int(screen_w/cell_s)  # Used in for loops, because a list starts with 0 then 1
cells_y_l = int(screen_h/cell_s)  # Used in for loops, because a list starts with 0 then 1
cells_x = cells_x_l - 1  # Used for checking neighbors
cells_y = cells_y_l - 1  # Used for checking neighbors
cells = [[0 for x in range(cells_x_l)] for y in range(cells_y_l)]
cells_new = cells

for x in range(cells_x_l):
    for y in range(cells_y_l):
        if random.randint(0, 9) == 1:  # Randomly fill in cells
            cells[x][y] = 1

screen.fill(c_white)
pg.display.update()


# Count cell nearest neighbors
def count_cells(x_cell, y_cell, radius):
    value = 0
    

    return value

while True:
    for x in range(cells_x_l):
        for y in range(cells_y_l):
            #if cells[x][(y - 1)] == 1:

            # WORKING CONFIGURATIONS
            # if cells[x][((y + 1) % cells_x)] == 1: # Down
            # if cells[((x + 1) % cells_x)][y] == 1: # Right
            # if cells[((x + 1) % cells_x)][((y + 1) % cells_y)] == 1: # Down right

            # if cells[((x + 1) % cells_x)][y] == 1:  # Right
            #     cells_new[x][y] = 1

            # print(cells[((x + 1) % cells_x)][y])
            if cells[((x + 1) % cells_x)][y] == 1: # Right
                cells_new[x][y] = 1
            # print(cells[x - 1][y])
            if cells[x - 1][y] == 1:
                cells_new[x][y] = 0

            if cells[x][y] == 1:
                pg.draw.rect(screen, c_black, (x * cell_s - cell_s_h, y * cell_s - cell_s_h, cell_s, cell_s), 0)
            elif cells[x][y] == 0:
                pg.draw.rect(screen, c_white, (x * cell_s - cell_s_h, y * cell_s - cell_s_h, cell_s, cell_s), 0)

    cells, cells_new = cells_new, cells

    pg.display.update()
    # pg.time.wait(10)
    # print(str(x) + ' ' + str(y))
    # pg.time.wait(1000)
    # pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
