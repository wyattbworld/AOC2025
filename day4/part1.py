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
for i in range(0, len(lines)):
    for j in range(0, len(lines[i])):
        if lines[i][j] == '@':
            total+= int(check_forklift(lines, i, j))

print(total)

