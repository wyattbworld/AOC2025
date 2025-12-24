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
    if line[0] == 'L':
        dial = (dial + int(line[1:])) % 100
    elif line[0] == 'R':
        dial = (dial - int(line[1:])) % 100
    else:
        print('Invalid text')
        exit()

    if dial == 0:
        hits+=1

print(hits) 