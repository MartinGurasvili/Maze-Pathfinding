import queue


# def createMaze():
#     maze = []
#     maze.append(["#","#", "#", "#", "#", "O","#"])
#     maze.append(["#"," ", " ", " ", "#", " ","#"])
#     maze.append(["#"," ", "#", " ", "#", " ","#"])
#     maze.append(["#"," ", "#", " ", " ", " ","#"])
#     maze.append(["#"," ", "#", "#", "#", " ","#"])
#     maze.append(["#"," ", " ", " ", "#", " ","#"])
#     maze.append(["#","#", "#", "#", "#", "X","#"])
# 
#     return maze

def createMaze2():
    maze = []
    
    maze.append([1,1,1,1,1,1,1,1,1])
    maze.append([1,0,0,0,0,0,0,0,1])
    maze.append([1,0,1,1,0,1,1,0,1])
    maze.append([1,0,1,0,0,0,1,0,1])
    maze.append([1,0,1,0,0,0,1,0,1])
    maze.append([1,2,1,0,0,0,1,0,1])
    maze.append([1,0,1,0,0,0,1,1,1])
    maze.append([1,0,0,0,0,0,0,0,1])
    maze.append([1,1,1,1,1,1,1,3,1])

    return maze


def printMaze(maze, path=""):
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
                maze[j][i] = 4
                
    for x in maze:
        print(x)
        


def valid(maze, moves,i,j):
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
        elif (maze[j][i] == 1):
            return False
        if maze[j][i] == 3:
            print("Found: " + moves)
            printMaze(maze, moves)
            found =True
            return True
    return True


def startp(maze,i,j):
    for x in range(len(maze[0])):
        try:
            i =(maze[x].index(2))
            j = x
            print(j)
            return i,j
        except:
            pass
# MAIN ALGORITHM
def solve():
    global grid
    nums = queue.Queue()
    nums.put("")
    add = ""
    
    i,ii =startp(grid,0,0)
    print(i,ii)
    print(type(grid))
    while True: 
        add = nums.get()
        for j in ["L", "R", "U", "D"]:
            put = add + j
            if valid(grid, put,i,ii):
                nums.put(put)
            if(found):
                break
            
grid = []
    
grid.append([1,1,1,1,1,1,1,1,1])
grid.append([1,0,0,0,0,0,0,0,1])
grid.append([1,0,1,1,0,1,1,0,1])
grid.append([1,2,1,0,0,0,1,0,1])
grid.append([1,0,1,0,0,0,1,0,1])
grid.append([1,0,1,0,0,0,1,0,1])
grid.append([1,0,1,0,0,0,1,1,1])
grid.append([1,0,0,0,0,0,0,0,1])
grid.append([1,1,1,1,1,1,1,3,1])
found = False                
solve()
