def solve1():
    file = open("AoC11.txt", "r")
    lines = [line.strip() for line in file.readlines()]

    n = len(lines)  # We have a square grid

    galaxies = []
    empty_cols = []
    empty_rows = []

    # Finding the galaxies
    for i in range(0, n):
        for j in range(0, n):
            if lines[i][j] == '#':
                galaxies.append([i, j])

    # Finding the empty rows
    for i in range(0, n):
        flag = True
        for galaxy in galaxies:
            if galaxy[0] == i:
                flag = False
                break
        if flag:
            empty_rows.append(i)

    # Finding the empty columns
    for i in range(0, n):
        flag = True
        for galaxy in galaxies:
            if galaxy[1] == i:
                flag = False
                break
        if flag:
            empty_cols.append(i)

    k = len(galaxies)

    rtn = 0
    for i in range(0, k):
        for j in range(i + 1, k):
            start = galaxies[i]
            end = galaxies[j]

            empty = 0
            for index in empty_rows:
                if min(start[0], end[0]) < index < max(start[0], end[0]):
                    empty += 1

            for index in empty_cols:
                if min(start[1], end[1]) < index < max(start[1], end[1]):
                    empty += 1

            rtn += 1 * empty + (max(start[0], end[0]) - min(start[0], end[0])) + (max(start[1], end[1]) - min(start[1], end[1]))

    return rtn


def solve2():
    file = open("AoC11.txt", "r")
    lines = [line.strip() for line in file.readlines()]

    n = len(lines)  # We have a square grid

    galaxies = []
    empty_cols = []
    empty_rows = []

    # Finding the galaxies
    for i in range(0, n):
        for j in range(0, n):
            if lines[i][j] == '#':
                galaxies.append([i, j])

    # Finding the empty rows
    for i in range(0, n):
        flag = True
        for galaxy in galaxies:
            if galaxy[0] == i:
                flag = False
                break
        if flag:
            empty_rows.append(i)

    # Finding the empty columns
    for i in range(0, n):
        flag = True
        for galaxy in galaxies:
            if galaxy[1] == i:
                flag = False
                break
        if flag:
            empty_cols.append(i)

    k = len(galaxies)

    rtn = 0
    for i in range(0, k):
        for j in range(i + 1, k):
            start = galaxies[i]
            end = galaxies[j]

            # Finding the number of empty rows/cols, they are identical in the problem
            empty = 0
            for index in empty_rows:
                if min(start[0], end[0]) < index < max(start[0], end[0]):
                    empty += 1

            for index in empty_cols:
                if min(start[1], end[1]) < index < max(start[1], end[1]):
                    empty += 1

            # This is the only number you have to change for part 2, just add a times 999999 multiplier
            rtn += 999999 * empty + (max(start[0], end[0]) - min(start[0], end[0])) + (max(start[1], end[1]) - min(start[1], end[1]))

    return rtn
