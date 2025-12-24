
'''
Author: C.Wyatt Bruchhauer
Date: December 24, 2025
'''
def find_invalid_code(code: str) -> bool:
    if code.startswith('0'):
        return True
    if len(code) % 2 != 0:
        return False
    if code[0: len(code)//2] == code[len(code)//2: len(code)]:
        print(code[0: len(code)//2], '=', code[len(code)//2: len(code)])
        return True
    else:
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
