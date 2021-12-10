class Node:
    def __init__(self, value):
        self.value = value
        self.marked = False  # marked as true when the node value is less than everything around it

    def get_value(self):
        return self.value

    def get_marked(self):
        return self.marked

    def set_marked(self, marked):
        self.marked = marked


def print_nodes(node_array):
    for i in range(len(node_array)):
        for j in range(len(node_array[i])):
            print(node_array[i][j].get_value(), end='')
        print()


def print_marked_nodes(node_array):
    for i in range(len(node_array)):
        for j in range(len(node_array[i])):

            if node_array[i][j].get_marked():
                print(node_array[i][j].get_value(), end=" ")
            else:
                print("N", end=" ")

        print()

    print()


def get_answer(node_array):
    ans = 0
    for i in range(len(node_array)):
        for j in range(len(node_array[i])):
            if node_array[i][j].get_marked():
                ans += 1 + int(node_array[i][j].get_value())

    return ans


with open('input.txt', 'r') as f:
    input_data = f.readlines()
    node_array = []

    # create number array
    for i in range(len(input_data)):
        input_data[i] = input_data[i].strip()
        input_data[i] = list(input_data[i])

    # create node array
    for i in range(len(input_data)):
        node_array.append([])
        for j in range(len(input_data[i])):
            node_array[i].append(Node(input_data[i][j]))

    print_nodes(node_array)

    print()

    # mark nodes if the value is less than everything around it
    for i in range(len(node_array)):
        for j in range(len(node_array[i])):
            curr_val = node_array[i][j].get_value()
            # i -> row
            # j -> col

            # check node above current one
            above_col = i-1
            if above_col >= 0 and above_col < len(node_array):
                # check if the node is less than the value
                if curr_val >= node_array[above_col][j].get_value():
                    continue

            # check node to the right
            right_row = j+1
            if right_row >= 0 and right_row < len(node_array[i]):
                if curr_val >= node_array[i][right_row].get_value():
                    continue

            # check node on the bottom
            below_col = i+1
            if below_col >= 0 and below_col < len(node_array):
                # check if the node is less than the value
                if curr_val >= node_array[below_col][j].get_value():
                    continue

            # check node to the left
            left_row = j-1
            if left_row >= 0 and left_row < len(node_array[i]):
                if curr_val >= node_array[i][left_row].get_value():
                    continue

            # node must be smaller than the values around it
            node_array[i][j].set_marked(True)

    print_marked_nodes(node_array)

    ans = get_answer(node_array)
    print(ans)
