def findGammaRate(lst):
    final = ""
    temp_ones = 0
    temp_zeros = 0
    for i in range(12):
        # i is the index of each element we are looking at
        for binary in lst:
            if binary[i] == '1':
                temp_ones += 1
            else:
                temp_zeros += 1
        if temp_ones > temp_zeros:
            final += '1'
        else:
            final += '0'
        temp_ones = 0
        temp_zeros = 0

    return final

def findEpilsonRate(lst):
    final = ""
    temp_ones = 0
    temp_zeros = 0
    for i in range(12):
        # i is the index of each element we are looking at
        for binary in lst:
            if binary[i] == '1':
                temp_ones += 1
            else:
                temp_zeros += 1
        if temp_ones > temp_zeros:
            final += '0'
        else:
            final += '1'
        temp_ones = 0
        temp_zeros = 0
    
    return final

with open('input.txt', 'r') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()

    # find gamma
    gamma = findGammaRate(lines)
    epsilon = findEpilsonRate(lines)
    gamma_int = int(gamma, 2)
    epsilon_int = int(epsilon, 2)

    print(gamma_int * epsilon_int)