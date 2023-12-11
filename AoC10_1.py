def solve1():
    file = open("AoC10.txt", "r")
    lines = [line.strip() for line in file.readlines()]

    grid = []
    n = len(lines)
    for line in lines:
        row = []
        for char in line:
            row.append(char)
        grid.append(row)

    start = 0
    for i in range(0, n):
        for j in range(0, n):
            if grid[i][j] == 'S':
                start = i * n + j
    """
    The grid is a square 140 x 140, which is nice
    We wish to construct an adjacency list
    """

    cur = 0
    if start in getAdjacent(grid, start - n, n):
        cur = start - n
    elif start in getAdjacent(grid, start + 1, n):
        cur = start + 1
    elif start in getAdjacent(grid, start - 1, n):
        cur = start - 1
    elif start in getAdjacent(grid, start + n, n):
        cur = start + n

    prev = start
    length = 1
    while cur != start:
        length += 1
        for node in getAdjacent(grid, cur, n):
            if node != prev:
                prev = cur
                cur = node
                break

    return int(length / 2)


def getAdjacent(grid, index, n):
    i = int(index / n)
    j = index % n
    if not 0 <= i < n:
        return []
    char = grid[i][j]
    if char == '|':
        return [index - n, index + n]
    elif char == '-':
        return [index + 1, index - 1]
    elif char == 'L':
        return [index - n, index + 1]
    elif char == 'J':
        return [index - n, index - 1]
    elif char == '7':
        return [index + n, index - 1]
    elif char == 'F':
        return [index + n, index + 1]
    else:
        return []
