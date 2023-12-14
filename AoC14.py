def solve1():
    file = open("AoC14.txt", "r")
    lines = [line.strip() for line in file.readlines()]

    grid = []
    for line in lines:
        row = []
        for char in line:
            row.append(char)
        grid.append(row)

    n = len(grid)
    m = len(grid[0])

    # North
    for i in range(0, n):
        for j in range(0, m):
            if grid[i][j] == 'O':
                grid[i][j] = '.'
                new_height = i
                while new_height >= 0:
                    if grid[new_height][j] == '.':
                        new_height -= 1
                    else:
                        new_height += 1
                        break
                if new_height < 0:
                    new_height = 0
                grid[new_height][j] = 'O'

    """
    Finding the blocks and calculating load
    I know that I could have done this in the other loop
    But I don't care because it seems nicer somehow
    """

    rtn = 0
    for i in range(0, n):
        for j in range(0, m):
            if grid[i][j] == 'O':
                rtn += n - i

    return rtn


"""
Ideas for the second part
* I need a way to simulate cycles
* Then, I can try to find a repetition (This is the risk)
* Next, I use the power of mod to reduce the iterations necessary
* Finally I calculate the final arrangement's load
"""


def solve2():
    file = open("AoC14.txt", "r")
    lines = [line.strip() for line in file.readlines()]

    grid = []
    for line in lines:
        row = []
        for char in line:
            row.append(char)
        grid.append(row)

    n = len(grid)
    m = len(grid[0])

    previous = []
    gargantua = 1000000000

    first_index = 0
    second_index = 0
    for k in range(0, gargantua):
        cycle(grid, n, m)
        string = toString(grid, n, m)
        if string in previous:
            second_index = k + 1
            break
        else:
            previous.append(string)

    grid_string = toString(grid, n, m)
    for i in range(0, len(previous)):
        if previous[i] == grid_string:
            first_index = i + 1

    iterations = (gargantua - first_index) % (second_index - first_index)

    for i in range(iterations):
        cycle(grid, n, m)

    return computeLoad(grid, n, m)


def computeLoad(grid, n, m):
    rtn = 0
    for i in range(0, n):
        for j in range(0, m):
            if grid[i][j] == 'O':
                rtn += n - i
    return rtn


def toString(grid, n, m):
    rtn = ""
    for i in range(0, n):
        for j in range(0, m):
            rtn += grid[i][j]
    return rtn


def cycle(grid, n, m):
    # North
    for i in range(0, n):
        for j in range(0, m):
            if grid[i][j] == 'O':
                grid[i][j] = '.'
                new_height = i
                while new_height >= 0:
                    if grid[new_height][j] == '.':
                        new_height -= 1
                    else:
                        new_height += 1
                        break
                if new_height < 0:
                    new_height = 0
                grid[new_height][j] = 'O'

    # West
    for j in range(0, m):
        for i in range(0, n):
            if grid[i][j] == 'O':
                grid[i][j] = '.'
                new_width = j
                while new_width >= 0:
                    if grid[i][new_width] == '.':
                        new_width -= 1
                    else:
                        new_width += 1
                        break
                if new_width < 0:
                    new_width = 0
                grid[i][new_width] = 'O'

    # South
    for i in reversed(range(0, n)):
        for j in range(0, m):
            if grid[i][j] == 'O':
                grid[i][j] = '.'
                new_height = i
                while new_height < n:
                    if grid[new_height][j] == '.':
                        new_height += 1
                    else:
                        new_height -= 1
                        break
                if new_height >= n:
                    new_height = n - 1
                grid[new_height][j] = 'O'

    # East
    for j in reversed(range(0, m)):
        for i in range(0, n):
            if grid[i][j] == 'O':
                grid[i][j] = '.'
                new_width = j
                while new_width < m:
                    if grid[i][new_width] == '.':
                        new_width += 1
                    else:
                        new_width -= 1
                        break
                if new_width >= m:
                    new_width = m - 1
                grid[i][new_width] = 'O'
