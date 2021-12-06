with open("input.txt") as f:
    data = f.read().split(",")
    for i in range(len(data)):
        data[i] = int(data[i])

    for i in range(256):
        # go through each element and check if it is < 0,
        # if so, we add an 8 to the end of the list and do length++
        # if not, then we subtract 1 from the element

        length = len(data)
        for j in range(length):
            if data[j] <= 0:
                data[j] = 6
                data.append(8)
                length += 1
            else:
                data[j] -= 1

    print(len(data))
