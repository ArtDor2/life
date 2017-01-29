# Artur Dorovskikh 2017 Jan 27-28
# My first medium size project in python and in programming

import sys, pygame as pg, random  # , math
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
cells_x = int(screen_w/cell_s)
cells_y = int(screen_h/cell_s)
cells = [[0 for x in range(cells_x)] for y in range(cells_y)]
# for x in range(cells_x):
#     for y in range(cells_y):
#         cells = [x][y] = 0

cells_new = cells

for x in range(cells_x):
    for y in range(cells_y):
        if random.randint(0, 9) == 1:  # Randomly fill in cells
            cells[x][y] = 1

screen.fill(c_white)
pg.display.update()


# Count cell nearest neighbors
def cells_count(x_cell, y_cell, radius):
    value = 0
    # Left column
    #value += cells[p_left][p_up]# + cells[x_cell][p_up] + cells[p_right][p_up]
    # Center column
    #value += cells[p_left][y_cell] + cells[p_right][y_cell]
    # Right column
    #value += cells[p_left][p_down] + cells[x_cell][p_down] + cells[p_right][p_down]

    # ? Code for implementing >1 radius neighbors
    # for x in range(radius):
    #     for y in range(radius):
    #         if xx < 0:
    #             x_cell =
    return value

while True:
    # Compute the new matrix
      # Second matrix to store the computed old matrix
    for x in range(cells_x):
        for y in range(cells_y):
            # if cells[x][y] == 0:
            #     cells_new[x][y] = 1
            # else:
            #     cells_new[x][y] = 0
            # print(str(x) + ' ' + str(y))
            # pg.time.wait(1)
            # pg.display.update()

            # if x - 1 < 0:
            #     x = cells_x - 1

            #use "clock function": 50 in 12 with leftover

            if cells[x][(y - 1)] == 1:
                if cells[x][((y + 1) % cells_x)] == 1:
                    cells_new[x][y] = 1
            # else:
            #     cells_new[x][y] = 0

            # if cells_count(x, y, 1) == 1:  # Neighbors < 2
            #     cells_new[x][y] = 1
            #     if cells[x][y] == 1:
            #         pg.draw.rect(screen, c_white, (x * cell_s - cell_s_h, y * cell_s - cell_s_h, cell_s, cell_s), 0)
            # if cells_count(x, y, 1) == 2 or 3:  # Neighbors == 2 or 3
            #     cells_new[x][y] = 1
            #     if cells[x][y] == 0:
            #         pg.draw.rect(screen, c_black, (x * cell_s - cell_s_h, y * cell_s - cell_s_h, cell_s, cell_s), 0)
            # else:  # Neighbors > 3
            #     cells_new[x][y] = 0
            #     if cells[x][y] == 1:
            #         pg.draw.rect(screen, c_white, (x * cell_s - cell_s_h, y * cell_s - cell_s_h, cell_s, cell_s), 0)
            if cells[x][y] == 1:
                pg.draw.rect(screen, c_black, (x * cell_s - cell_s_h, y * cell_s - cell_s_h, cell_s, cell_s), 0)
            else:
                pg.draw.rect(screen, c_white, (x * cell_s - cell_s_h, y * cell_s - cell_s_h, cell_s, cell_s), 0)
        # pg.display.update()
        # pg.time.wait(10)
    cells, cells_new = cells_new, cells

    pg.display.update()
    #pg.time.wait(1000)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
