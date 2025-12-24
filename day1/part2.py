'''
Author: C.Wyatt Bruchhauer
Date: December 24, 2025
'''

input = None
with open('input.txt', 'r') as ifile:
    input = ifile.read()

lines = input.split('\n')

dial = 50
hits = 0

for line in lines:
    direction = line[0]
    change =  int(line[1:])

    if direction == 'L':
        change*=-1

    rotations = abs(dial+change) // 100
    if (dial+change <= 0) and (dial != 0):
        rotations += 1

    hits += rotations

    dial = (dial + change) % 100

print(hits) 