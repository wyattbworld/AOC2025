LIMIT = 12

def find_joltage(battery: str, limit: int) -> int:
    lastj = -1
    joltage = 0
    for i in range(limit, 0, -1):
        max: int = 0
        for j in range(lastj+1, len(battery)-i+1):
            if max < int(battery[j]):
                max = int(battery[j])
                lastj = j
        
        joltage += max * (10 ** (i-1))

    return joltage


input = None
with open('input.txt', 'r') as ifile:
    input = ifile.read()

lines = input.split('\n')

sum = 0
for line in lines:
    sum += find_joltage(line, LIMIT)

print(sum)