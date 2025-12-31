def check_forklift(lines: list[str], i: int, j: int) -> bool:
    total = 0
    width = len(lines[0])
    height = len(lines)
    
    #upleft
    if i > 0 and j > 0:
        if lines[i-1][j-1] == '@':
            total+=1
    
    #up
    if i > 0:
        if lines[i-1][j] == '@':
            total+=1
    
    #upright
    if i > 0 and j < width - 1:
        if lines[i-1][j+1] == '@':
            total+=1
    
    #left
    if j > 0:
        if lines[i][j-1] == '@':
            total+=1
    
    #right
    if j < width-1:
        if lines[i][j+1] == '@':
            total+=1
    
    #downleft
    if i < height-1 and j > 0:
        if lines[i+1][j-1] == '@':
            total+=1
    
    #down
    if i < height-1:
        if lines[i+1][j] == '@':
            total+=1

    #downright
    if i < height-1 and j < width -1:
        if lines[i+1][j+1] == '@':
            total+=1
    
    if total < 4:
        return True
    else:
        return False

input = None
with open('input.txt', 'r') as ifile:
    input = ifile.read()

lines = input.split('\n')

total = 0
while True:
    to_remove = []  
    for i in range(0, len(lines)):
        for j in range(0, len(lines[i])):
            if lines[i][j] == '@':
                if check_forklift(lines, i, j):
                    total+=1
                    to_remove.append([i, j])
    
    if not to_remove:
        break
    else:
        for item in to_remove:
            if item[1] < len(lines[0])-1:
                lines[item[0]] = lines[item[0]][:item[1]] + '.' + lines[item[0]][item[1]+1:]
            else:
                lines[item[0]] = lines[item[0]][:item[1]] + '.'

print(total)

