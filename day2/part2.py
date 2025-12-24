'''
Author: C.Wyatt Bruchhauer
Date: December 24, 2025
'''

def find_invalid_code(code: str) -> bool:
    if code.startswith('0'):
        return True
    for i in range(2, len(code)+1):
        if len(code) % i != 0:
            continue
        first_piece = code[0:len(code)//i]
        is_invalid = True
        for j in range(len(code)//i, len(code), len(code)//i):
            if code[j:j+len(code)//i] != first_piece:
                is_invalid = False
                break 
        if is_invalid:
            return True
    return False
    

input = None
with open('input.txt', 'r') as ifile:
    input = ifile.read()

lines = input.split(',')

sum = 0
for line in lines:
    start = int(line.split('-')[0])
    end = int(line.split('-')[1]) + 1 #non inclusive
    for code in range(start, end):
        if find_invalid_code(str(code)):
            sum += code
    
print(sum)
