def check(checkVar):
    if checkVar == '*':
        return 1
    if checkVar == '.':
        return 2
    else:
        return 3

def isFill(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if(grid[i][j] == '.'):
                return False
    
    return True

def isPositionValid(count, i, j, grid):
    if i==0 or j==0 or i==len(grid) or j==len(grid[i]):
        if i>0 and j>0 and j-1<len(grid[i]) and i-1<len(grid):
            if grid[i-1][j]=='*' or grid[i-1][j+1]=='*' or grid[i-1][j-1]=='*' or grid[i][j-1]=='*' or grid[i][j+1]=='*' or grid[i+1][j+1]=='*' or grid[i+1][j-1]=='*' or grid[i+1][j-1]=='*':
                return False
            else:
                if grid[i-1][j]=='.':
                    isPositionValid(count+1, i-1, j, grid)
                if grid[i-1][j+1]=='.':
                    isPositionValid(count+1, i-1, j+1, grid)
                if grid[i-1][j-1]=='.':
                    isPositionValid(count+1, i-1, j-1, grid)
                if grid[i][j-1]=='.':
                    isPositionValid(count+1, i, j-1, grid)
                if grid[i][j+1]=='.':
                    isPositionValid(count+1, i, j+1, grid)
                if grid[i+1][j]=='.':
                    isPositionValid(count+1, i+1, j, grid)
                if grid[i+1][j-1]=='.':    
                    isPositionValid(count+1, i+1, j-1, grid)
                if grid[i+1][j+1]=='.':    
                    isPositionValid(count+1, i+1, j+1, grid)
                grid[i][j] = str(count)
    else:
        return True


inputFile = open('input.txt', 'r')
outputFile = open('output.txt', 'w')

testCase = int(inputFile.readline())
Case = 1
while testCase > 0:
    inputString = inputFile.readline().split(" ")

    grid = []
    for i in range(int(inputString[0])):
        temp = []
        for j in range(int(inputString[1])):
            temp.append('.')
        grid.append(temp)

    mines = int(inputString[2])

    if mines > 0:
        for i in range(int(inputString[0])):
            for j in range(int(inputString[1])):
                grid[i][j] = '*'
                mines -= 1
                if mines == 0:
                    break
            if mines == 0:
                break
        
        for i in range(int(inputString[0])):
            for j in range(int(inputString[1])):
                if check(grid[i][j]) == 1:
                    continue
                elif check(grid[i][j]) == 2:
                    grid[i][j] = 'c'
                    if isPositionValid(0, i, j, grid):
                       print(i, j)
                       break
                else:
                    outputFile.write('Case #' + str(Case) + ':' '\nImpossible\n')
                    print('bhbshb')
                    break
        
        if isFill(grid):
            outputFile.write('Case #' + str(Case) + ': \n')
            for i in range(int(inputString[0])):
                for j in range(int(inputString[1])):
                    outputFile.write(grid[i][j])
                outputFile.write('\n')
        else:
            outputFile.write('Case #' + str(Case) + ':' '\nImpossible\n')
            print('Hel')


    else:
        grid[0][0] = 'c'
        outputFile.write('Case #' + str(Case) + ': \n')
        for i in range(int(inputString[0])):
            for j in range(int(inputString[1])):
                outputFile.write(grid[i][j])
            outputFile.write('\n')

    Case += 1
    testCase -= 1
