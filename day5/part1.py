input = None
with open('input.txt', 'r') as ifile:
    input = ifile.read()

lines = input.split('\n')

ranges = []
values = []
is_range = True
for line in lines:
    if '-' not in line:
        is_range = False
    
    if is_range:
        ranges.append(list(map(int, line.split('-'))))
    elif line:
        values.append(int(line))
    

total = 0

for value in values:
    for range in ranges:
        if value >= range[0] and value <= range[1]:
            total+=1
            break

print(total)