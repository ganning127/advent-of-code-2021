horiz = 0
depth = 0
aim = 0

with open("input.txt", "r") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()

        direct, val = lines[i].split(" ")
        if direct == "up":
            aim -= int(val)
        elif (direct == "down"):
            aim+= int(val)
        elif (direct == "forward"):
            horiz += int(val)
            depth += (aim * int(val))
        
    print(horiz * depth)
