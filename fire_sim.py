# Project 10 - Fire Simulation
# CSC 110, Spring 2018
# This project simulates fire behaviour spread to an extent. By the use of 2d
# lists, its traversals and loops the program intakes data file and reads it,
# calculates and demonstrates the fire spread through animation with Drawing
# Panel.

import random
from DrawingPanel import *


# The body of the program, dictates by steps and a while loop the behaviour
# of the program.
# PARAMS: none
# RETURN: none
def main():
    linez = data_extract()
    grid = grid_create(linez)
    draw_grid(grid)
    flag = 0   
    while flag != 1:
        null = null_grid(grid)
        fire_off(grid,null)
        spark(grid,null)
        grid = null
        draw_grid(grid)
        flag=1
        for row in grid:
            for col in row:
                if col == '2':
                    flag = 0


# Ask user for file name, extracts the data from file and reads it by lines
# PARAMS: none
# RETURN: lines from read file
def data_extract():
    inputz = input("file name?: ")     
    lines = open(inputz).readlines() 
    return (lines)

# Takes lines from a file, cleans then and appends to a 2d list
# PARAMS: lines from data file
# RETURN: file name data in 2d list
def grid_create(lines):
    exo_lizt = []
    for line in lines:
        line = line.strip().split(' ')
        endo_lizt = []
        for digit in line:
            endo_lizt.append(digit)
        exo_lizt.append(endo_lizt) #make lizt of lizt!
    return (exo_lizt)

# Copies the size and height of Original grid, full of 0's
# PARAMS: Grid fromed from grid_create
# RETURN: Parallel grid in size, ready to be populated by new string values.

def null_grid(grid):   
    y = len(grid)
    x = len(grid[0])
    null = []
    for i in range(y):
        null.append(['0']*x)
    return (null)

# Populates null grid with original grid while replacing 'fire'(2) with a 0
# PARAMS: intakes populated grid and 'empty' grid (nul grid)
# RETURN: newly populated null grid
def fire_off(grid,null):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            null[i][j] = grid[i][j]
            if grid[i][j] == '2' :
                null[i][j] = '0'
    return null

# Iterates through grid checking for neighboring "fire"(2). If locates,
# sparks "tree"(1) if criteria is met, otherwise leaving it alone. Populates
# null grid with newer data, changing trees to fire if they catch spark
# PARAMS: intakes populated grid and modified nul grid
# RETURN: none
def spark(grid,null):       
    for i in range(len(grid)-1):
        for j in range(len(grid[i])-1):             
            north = grid[i-1][j] 
            south = grid[i+1][j]               
            east = grid[i][j+1] 
            west = grid[i][j-1]
            if grid[i][j] == '1' :
                if north == '2' or south=='2' or east=='2' or west=='2':
                    spark = random.randint(1,100)
                    if spark < 75:
                        null[i][j] = '2'
    return null

# takes grid and outputs on Drawing Panel according to string values within
# grid. Sleeps imaging by 100 miliseconds to animate fire spread
# PARAMS: Takes in grid for drawing specifics and "p", the drawing panel to
# further use for inputing onto DrawingPanel
# RETURN: none
def draw_grid(grid):
    p = DrawingPanel(130,130,background='light gray')
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            x= j * 10
            y= i * 10
            if grid[i][j] == '0':
                p.fill_rect(x,y, 10,10, 'yellow')
            elif grid[i][j] == '1' :
                p.fill_rect(x,y, 10,10, 'green')
            else:
                p.fill_rect(x,y, 10,10, 'red')
    p.sleep(100)
                

main()
