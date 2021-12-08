def median(lst):
    if len(lst) % 2 == 0:  # Checking if the length is even
        # Applying formula which is sum of middle two divided by 2
        return (lst[len(lst) // 2] + lst[(len(lst) - 1) // 2]) / 2
    else:
        # If length is odd then get middle value
        return lst[len(lst) // 2]


with open("input.txt") as f:
    crabs = f.read().split(",")
    for i in range(len(crabs)):
        crabs[i] = int(crabs[i])

    crabs.sort()
    fuel_used = 0
    optimal = median(crabs)

    for i in range(len(crabs)):
        fuel_used += abs(optimal - crabs[i])

    print(fuel_used)
