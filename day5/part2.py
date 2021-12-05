with open("input.txt", "r") as f:
    data = f.readlines()
    for i in range(len(data)):
        line = data[i].strip().split(" -> ")
        # print(line)
        line_start = line[0].split(",")
        line_end = line[1].split(",")
        line = [line_start, line_end]
        data[i] = line

    # data is a 3D list
    # find the max x and max y value
    max_x = 0
    max_y = 0
    for i in range(len(data)):
        for coord in data[i]:
            if int(coord[0]) > max_x:
                max_x = int(coord[0])
            if int(coord[1]) > max_y:
                max_y = int(coord[1])

    # create an array of 0-989 and 0-989
    grid = [[0 for x in range(max_x+1)] for y in range(max_y + 1)]
    for set_corrds in data:
        start_x = int(set_corrds[0][0])
        start_y = int(set_corrds[0][1])
        end_x = int(set_corrds[1][0])
        end_y = int(set_corrds[1][1])
        if start_x == end_x:
            # vertical line, so fill in vertically
            for i in range(min(start_y, end_y), max(start_y, end_y)+1):
                grid[start_x][i] += 1

        elif start_y == end_y:
            # horizontal line, so fill in horizontally
            for i in range(min(start_x, end_x), max(start_x, end_x)+1):
                grid[i][start_y] += 1

        else:
            x = start_x  # tehcnically "start"
            y = start_y
            grid[x][y] += 1
            while x != end_x or y != end_y:
                if start_x < end_x:
                    x += 1
                else:
                    x -= 1

                if start_y < end_y:
                    y += 1
                else:
                    y -= 1

                grid[x][y] += 1
                # iterate through every elemnent in the grid
                # if it's > 0, print it
    counter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] >= 2:
                counter += 1
    print(counter)
