with open('input.txt', 'r') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = int(lines[i].strip())

    counter = 0
    for i in range(2, len(lines)-1):
        sum1 = lines[i-2] + lines[i-1] + lines[i]
        sum2 = lines[i-1] + lines[i] + lines[i+1]
        if sum2>sum1:
            counter += 1

    print(counter)