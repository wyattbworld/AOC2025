
def runion(base: list, add: list):
    for i in range(len(base)):
        if not (add[0] > base[i][1] or base[i][0] > add[1]):
            newran = [min(base[i][0], add[0]), max(base[i][1], add[1])]
            base.pop(i)
            return runion(base, newran)
        
    base.append(add)
    return base



input = None
with open('input.txt', 'r') as ifile:
    input = ifile.read()

lines = input.split('\n')
ranges = [] #
iranges = []
is_range = True
for line in lines:
    if '-' not in line:
        break
    ranges.append(list(map(int, line.split('-'))))


oranges = list()

for ran in ranges:
    oranges = runion(oranges, ran)

total = 0
for ran in oranges:
    total += ran[1] - ran[0] + 1

print(total)