from itertools import count
import pygame
import numpy as np
from queue import PriorityQueue
import queue
import os
import sys

#colors
one = (79, 189, 186)
two = (206, 171, 147)
three = (227, 202, 165)
four = (255, 251, 233)
five = (246, 137, 137)
six = (255, 0, 0)
seven = (0, 255, 0)

pygame.init()

size = (706, 706)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("MAZE")

width = 20
height = 20
margin = 2

grid = [[0 for x in range(33)] for y in range(33)]

done = False
clock = pygame.time.Clock()
found = False
neighbour=[]

def savegrid():
    global grid
    np.savetxt(r"./Downloads/Maze-Pathfinding-main/maze.txt",grid)
def loadgrid(index):
    global grid
    if(index ==0):
        grid = np.loadtxt(r"./Downloads/Maze-Pathfinding-main/maze.txt").tolist()
    elif(index ==1):
        grid = np.loadtxt(r'./Downloads/Maze-Pathfinding-main/Maze1/maze.txt').tolist()
    elif(index ==2):
        grid = np.loadtxt(r'./Downloads/Maze-Pathfinding-main/Maze2/maze.txt').tolist()
    elif(index ==3):
        grid = np.loadtxt(r'./Downloads/Maze-Pathfinding-main/Maze3/maze.txt').tolist()
    elif(index ==4):
        grid = np.loadtxt(r'./Downloads/Maze-Pathfinding-main/Maze4/maze.txt').tolist()
    elif(index ==5):
        grid = np.loadtxt(r'./Downloads/Maze-Pathfinding-main/Maze5/maze.txt').tolist()
        
def bfs_shortestpath(maze, path=""):
    global grid
    i,j=startp(maze,0,0)
    pos = set()
    for move in path:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j, i))
    
    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in pos:
                
                grid[j][i] = 4
                
def startp(maze,i,j):
    for x in range(len(maze[0])):
        try:
            i =(maze[x].index(2))
            j = x
            print(j)
            return i,j
        except:
            pass

def bfs(maze, moves,i,j):
    global found
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == 1.0):
            return False
        if maze[j][i] == 3:
            print("Found: " + moves)
            bfs_shortestpath(maze, moves)
            found =True
            return True
            break
    return True


def bfs_solve():
    global grid
    nums= queue.Queue()
    nums.put("")
    add = ""
    i,ii =startp(grid,0,0)
    while found != True: 
        add = nums.get()
        for j in ["L", "R", "U", "D"]:
            put = add + j
            if bfs(grid, put,i,ii):
                nums.put(put)
            if(found == True):
                break
            
def neighbourr():
    global grid,neighbour
    neighbour = [[]for col in range(len(grid)) for row in range(len(grid))]
    count=0
    for i in range(len(grid)):
        for j in range(len(grid)):
            neighbour[count] == []
            if (i > 0 and grid[i - 1][j] != 1):
                neighbour[count].append((i-1,j))
            if (j > 0 and grid[i][j - 1] != 1):
                neighbour[count].append((i,j-1))
            if (i < len(grid) - 1 and grid[i + 1][j] != 1):
                neighbour[count].append((i+1,j))
            if (j < len(grid) - 1 and grid[i][j + 1] != 1):
                neighbour[count].append((i,j+1))
            count+=1
            
            
    
            
def h(p1, p2):
	x1, y1 = p1
	x2, y2 = p2
	return abs(x1 - x2) + abs(y1 - y2)

def S_E(maze,start,end):
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if(grid[x][y]==2):
                start =x,y
            if(grid[x][y]==3):
                end =x,y
       
    return start,end

def short_path(came_from, current):
     grid[current[0]][current[1]] = 4
     while current in came_from:
         current = came_from[current]
         grid[current[0]][current[1]] = 4
        
    
        
def a_star():
    global grid, neighbour
    neighbourr()

    start,end = S_E(grid,0,0)
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    open_set_his = {start}
    came_from = {}
    
    g_score = [float("inf") for row in grid for spot in row ]
    g_score[start[0]*len(grid[0]) +start[1]] = 0
    f_score = [ float("inf") for row in grid for spot in row ]
    f_score[start[0]*len(grid[0]) +start[1]] = h(start, end)

    
    while not open_set.empty():
        current = open_set.get()[2]
        open_set_his.remove(current)
        if current == end:
            print("finishing")
            short_path(came_from, end)
            return True
        for nei in neighbour[current[0]*len(grid[0]) +current[1]]:
            temp_g_score = g_score[current[0]*len(grid[0]) +current[1]] + 1
            if temp_g_score < g_score[nei[0]*len(grid[0]) +nei[1]]:
                came_from[nei] = current
                g_score[nei[0]*len(grid[0]) +nei[1]] = temp_g_score
                f_score[nei[0]*len(grid[0]) +nei[1]] = temp_g_score + h(nei, end)
                if nei not in open_set_his:
                    count += 1
                    open_set.put((f_score[nei[0]*len(grid[0]) +nei[1]], count, nei))
                    open_set_his.add(nei)
                    # grid[nei[0]][nei[1]] = 5
                    # pygame.display.update()
                    # time.sleep(0.01)
    
        # if current != start:
        #     grid[current[0]][current[1]] = 6
        #     pygame.display.update()
        #     time.sleep(0.01)
        

    return False


while not done:

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
             if event.key == pygame.K_ESCAPE:
                    print("Exit")
                    pygame.quit()
             if event.key == pygame.K_s:
                 print("Saving Maze")
                 savegrid()
             if event.key == pygame.K_l:
                 print("Loading Maze")
                 loadgrid(0)
             if event.key == pygame.K_f:
                 print("Filling Maze")
                 grid = [[1 for x in range(33)] for y in range(33)]
             if event.key == pygame.K_1:
                 print("Loading Maze 1")
                 loadgrid(1)
             if event.key == pygame.K_2:
                 print("Loading Maze 2")
                 loadgrid(2)
             if event.key == pygame.K_3:
                 print("Loading Maze 3")
                 loadgrid(3)
             if event.key == pygame.K_4:
                 print("Loading Maze 4")
                 loadgrid(4)
             if event.key == pygame.K_5:
                 print("Loading Maze 5")
                 loadgrid(5)
             if event.key == pygame.K_RETURN:
                if((sum(x.count(2) for x in grid)) == 1):
                    print("Solving")
                    # bfs_solve()
                    a_star()
             if event.key == pygame.K_r:

                grid = [[0 for x in range(33)] for y in range(33)]
        if pygame.mouse.get_pressed()[2]:
            column = pos[0] // (width + margin)
            row = pos[1] // (height + margin)
            if((sum(x.count(2) for x in grid)) < 1 or (sum(x.count(3) for x in grid)) < 1):
                if((sum(x.count(2) for x in grid)) == 0):
                    if(grid[row][column] == 2):
                        grid[row][column] = 0
                    elif(grid[row][column] == 3):
                        grid[row][column] = 0
                    else:
                        grid[row][column]  = 2
                else:
                    if(grid[row][column] == 3):
                        grid[row][column] = 0
                    elif(grid[row][column] == 2):
                        grid[row][column] = 0
                    else:
                        grid[row][column]  = 3
            else:
                if(grid[row][column] == 2):
                    grid[row][column] = 0
                if(grid[row][column] == 3):
                    grid[row][column] = 0
                if(grid[row][column] == 1):
                    grid[row][column] = 0
        if pygame.mouse.get_pressed()[0]:
            # if(event.button == 1):
            column = pos[0] // (width + margin)
            row = pos[1] // (height + margin)
            print("left click")
            grid[row][column] = 1
        
                
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
    screen.fill(two)
    for row in range(33):
        for column in range(33):
            if grid[row][column] == 1:
                color = three
            elif grid[row][column] == 2:
                color = one
            elif grid[row][column] == 3:
                color = five
            elif grid[row][column] == 4:
                color = one
            elif grid[row][column] == 5:
                color = six
            elif grid[row][column] == 6:
                color = seven
            else:
                color = four
            pygame.draw.rect(screen, color, [margin + (margin + width) * column, margin + (margin + height) * row, width, height])
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
