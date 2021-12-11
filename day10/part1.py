import math
from os import close
scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

illegal = []


def check_syntax(strings):
    open_list = ["[", "{", "(", "<"]

    mapper = {
        "[": "]",
        "{": "}",
        "(": ")",
        "<": ">",
    }
    illegal = []

    for string in strings:
        stack = []
        for char in string:
            if char in open_list:
                # is open character
                stack.insert(0, char)
            else:
                # is a close character, check if the top of the stack matches
                top = stack.pop(0)
                if mapper[top] != char:
                    # print("top:", mapper[top], "char:", char)
                    illegal.append(char)
                    break

    return illegal


def get_score(lst):
    sum = 0
    for char in lst:
        sum += scores[char]
    return sum


with open("input.txt", "r") as f:
    data = f.readlines()
    for i in range(len(data)):
        data[i] = data[i].strip()

    illegals = check_syntax(data)
    score = get_score(illegals)
    print(score)
