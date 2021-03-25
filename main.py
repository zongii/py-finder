file = open("file.txt", "r").readlines()

board = []

allPaths = []
allSteps = []

def initBoard(width, length, starting):
    global file
    global board

    board.clear()

    for i in range(starting, starting+length):
        temp = "{:<"+str(width)+"}"
        emptystring = temp.format(file[i].rstrip())
        board.append(emptystring)

def getStartCoords(brd):
    ln = 0

    for l in brd:
        wd = 0
        for c in l:
            if c == 'o':
                return [wd, ln]
            wd +=1
        ln += 1

def pathfind(x, y, path, iteration, width, length):
    global allPaths
    global allSteps
    global board
    if x <= 0 or width >= x and y <= 0 or length >= y:
        if board[y][x] != '#':
            if [x, y] not in path:
                path.append([x, y])
                if board[y][x] == 'X':
                    allPaths.append(iteration)
                    allSteps.append(path.copy())
                    return
                pathfind(x, y-1, path.copy(), iteration+1, width, length)
                pathfind(x, y+1, path.copy(), iteration+1, width, length)
                pathfind(x-1, y, path.copy(), iteration+1, width, length)
                pathfind(x+1, y, path.copy(), iteration+1, width, length)

def writePath(path):
    global board
    for coords in path:
        templist = list(board[coords[1]])
        if templist[coords[0]] == ' ':
            templist[coords[0]] = '.'
        board[coords[1]] = ''.join(templist)

boardscount = int(file[0].rstrip())
currentindex = 1

running = True

while running:
    boardscount -= 1
    if boardscount <= 0:
        running = False

    cfgVar = file[currentindex].rstrip().split(" ")
    glWidth = int(cfgVar[0])
    glLength = int(cfgVar[1])

    initBoard(glWidth, glLength, currentindex+1)
    crds = getStartCoords(board)
    pathfind(crds[0], crds[1], [], 1, glWidth, glLength)

    writePath(allSteps[allPaths.index(sorted(allPaths)[0])])

    for l in board:
        print(l)

    allPaths.clear()
    allSteps.clear()

    currentindex += glLength+1