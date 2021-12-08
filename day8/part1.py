with open("input.txt", "r") as f:
    data = f.readlines()
    for i in range(len(data)):
        data[i] = data[i].strip().split(" | ")

    valids = [2, 4, 3, 7]

    counter = 0
    for item in data:
        item_list = item[1].split(" ")  # only looking at outputs
        for output in item_list:
            if len(output) in valids:
                counter += 1

    print(counter)
