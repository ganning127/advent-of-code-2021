import math
from os import close
scores = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

illegal = []


def clean(strings):
    cleaned = strings.copy()
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
                    cleaned.remove(string)

    return cleaned  # items in here are incomplete, not corrupted


def check_syntax(strings):
    open_list = ["[", "{", "(", "<"]

    mapper = {
        "[": "]",
        "{": "}",
        "(": ")",
        "<": ">",
    }

    needed_to_close = []

    for string in strings:
        stack = []
        for char in string:
            if char in open_list:
                # is open character
                stack.insert(0, char)
            else:
                # is a close character, check if the top of the stack matches
                stack.pop(0)
        nested = []
        for char in stack:
            nested.append(mapper[char])
        needed_to_close.append(nested)

    return needed_to_close  # items in the stack


def get_score(arr):
    scores_lst = []
    for string in arr:
        score = 0
        for char in string:
            score *= 5
            score += scores[char]
        scores_lst.append(score)

    scores_lst.sort()
    return scores_lst[math.floor(len(scores_lst)/2)]


with open("input.txt", "r") as f:
    data = f.readlines()
    for i in range(len(data)):
        data[i] = data[i].strip()

    cleaned = clean(data)
    needed_to_close = check_syntax(cleaned)
    score = get_score(needed_to_close)
    print(score)
