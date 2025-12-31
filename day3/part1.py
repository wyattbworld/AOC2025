def find_joltage(battery: str) -> int:
    max = 0
    maxi = 0
    for i in range(0, len(battery)-1):
        jolt = int(battery[i])
        if jolt > max:
            max = jolt
            maxi = i
    
    dig_one = max

    max = 0
    for i in range(maxi+1, len(battery)):
        jolt = int(battery[i])
        if jolt > max:
            max = jolt
    
    return dig_one * 10 + max

input = None
with open('input.txt', 'r') as ifile:
    input = ifile.read()

lines = input.split('\n')

sum = 0
for line in lines:
    sum += find_joltage(line)

print(sum)