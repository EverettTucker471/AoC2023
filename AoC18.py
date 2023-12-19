import re


def solve1():
    file = open("AoC18.txt", "r")
    lines = [line.strip() for line in file.readlines()]

    num_regex = re.compile(r'\d+')
    data = []
    for line in lines:
        data.append((line[0], int(num_regex.findall(line)[0])))

    grid = []
    size = 500
    for i in range(size):
        row = []
        for j in range(size):
            row.append(Point(i, j))
        grid.append(row)

    i = int(size / 2)
    j = int(size / 2)

    for move in data:
        for k in range(move[1]):
            grid[i][j].explored = True
            if move[0] == 'L':
                j += 1
            elif move[0] == 'R':
                j -= 1
            elif move[0] == 'U':
                i -= 1
            elif move[0] == 'D':
                i += 1

    rtn = 0
    queue = [[0, 0]]
    while len(queue) > 0:
        node = queue.pop()
        i = node[0]
        j = node[1]

        if grid[i][j].explored:
            continue

        rtn += 1
        grid[i][j].explored = True

        # Left
        if 0 < j and grid[i][j - 1].explored is False:
            queue.append([i, j - 1])

        # Right
        if j < size - 1 and grid[i][j + 1].explored is False:
            queue.append([i, j + 1])

        # Up
        if 0 < i and grid[i - 1][j].explored is False:
            queue.append([i - 1, j])

        # Down
        if i < size - 1 and grid[i + 1][j].explored is False:
            queue.append([i + 1, j])

    return size ** 2 - rtn


def printGrid(grid, size):
    for i in range(size):
        row = ""
        for j in range(size):
            if grid[i][j].explored:
                row += '#'
            else:
                row += '.'
        print(row)


class Point:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.explored = False


def solve2():
    """
    You have to do this with Green's Theorem
    :return:
    """
    file = open("AoC18.txt", "r")
    lines = [line.strip() for line in file.readlines()]

    regex = re.compile(r'\(.*\)')
    data = []
    for line in lines:
        data.append(regex.findall(line)[0][2:].strip(')'))

    pairs = []
    for move in data:
        pairs.append([move[-1], toHex(move[:-1])])

    return compute(pairs)


def compute(pairs):
    rtn = 0
    x = 0
    for pair in pairs:
        if pair[0] == '0' or pair[0] == 'R':
            x += pair[1]
            rtn += pair[1]
        elif pair[0] == '1' or pair[0] == 'D':
            rtn += (x + 1) * pair[1]
        elif pair[0] == '2' or pair[0] == 'L':
            x -= pair[1]
        elif pair[0] == '3' or pair[0] == 'U':
            rtn -= x * pair[1]

    return rtn + 1


def toHex(word):
    rtn = 0
    exp = 1
    map = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'a': 10,
        'b': 11,
        'c': 12,
        'd': 13,
        'e': 14,
        'f': 15
    }
    for char in reversed(word):
        rtn += exp * map[char]
        exp *= 16
    return rtn
