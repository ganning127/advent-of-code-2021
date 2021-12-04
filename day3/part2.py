def getMostCommonBit(lines, i):
    zeros = 0
    ones = 0

    for j in range(len(lines)):
        if lines[j][i] == '0':
            zeros += 1
        else:
            ones += 1
    
    if ones >= zeros:
        return '1'
    else:
        return '0'


def getOxy(lines):
    for i in range(len(lines[0])):
        most_common = getMostCommonBit(lines, i)
        print("most common " + most_common)

        for line in lines:
            if line[i] != most_common:
                lines.remove(line)
            
            if len(lines) == 1:
                return i

with open('input.txt', 'r') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()


    oxy = getOxy(lines)
    print(lines)