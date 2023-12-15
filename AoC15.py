import re


def solve1():
    file = open("AoC15.txt", "r")
    line = file.readline().strip()

    rtn = 0
    for string in line.split(','):
        rtn += hashcode(string)

    return rtn


"""
Part 2 is almost completely different
The boxes are lists of tuples (chars, focal length)
The hashes correspond to the box numbers, but they just use the characters
"""


def solve2():
    file = open("AoC15.txt", "r")
    line = file.readline().strip()

    boxes = []
    for i in range(256):
        boxes.append([])

    string_regex = re.compile(r'\w+')
    number_regex = re.compile(r'\d')

    # Filling the boxes
    for string in line.split(','):
        characters = string_regex.findall(string)[0]
        code = hashcode(characters)
        if string.find('=') >= 0:
            flag = True
            for box in boxes[code]:
                if box[0] == characters:
                    box[1] = int(number_regex.findall(string)[0])
                    flag = False
                    break
            if flag:
                boxes[code].append([characters, int(number_regex.findall(string)[0])])
        else:
            for box in boxes[code]:
                if box[0] == characters:
                    boxes[code].remove(box)
                    break

    # Calculating the final answer
    rtn = 0
    for i in range(0, 256):
        for j in range(0, len(boxes[i])):
            rtn += (i + 1) * (j + 1) * boxes[i][j][1]

    return rtn


def hashcode(string):
    rtn = 0
    for char in string:
        rtn += ord(char)
        rtn = (17 * rtn) % 256
    return rtn
