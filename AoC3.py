def solve1():
    file = open("AoC3.txt", "r")
    lines = [line.strip() for line in file.readlines()]

    list = []
    for line in lines:
        row = []
        for char in line:
            row.append(char)
        list.append(row)

    rows = len(list)
    cols = len(list[0])

    adjacent = set()

    for i in range(0, rows):
        for j in range(0, cols):
            val = list[i][j]
            if not val.isdigit() and val != '.':
                adjacent.add((i - 1) * rows + j - 1)
                adjacent.add((i - 1) * rows + j)
                adjacent.add((i - 1) * rows + j + 1)
                adjacent.add(i * rows + j - 1)
                adjacent.add(i * rows + j + 1)
                adjacent.add((i + 1) * rows + j - 1)
                adjacent.add((i + 1) * rows + j)
                adjacent.add((i + 1) * rows + j + 1)

    rtn = 0
    for i in range(0, rows):
        power = 0
        num = 0
        flag = False
        for j in reversed(range(0, cols)):
            val = list[i][j]
            if val.isdigit():
                num += int(val) * (10 ** power)
                power += 1
                if (rows * i + j) in adjacent:
                    flag = True
            else:
                if flag:
                    rtn += num
                power = 0
                num = 0
                flag = False

        if flag:
            rtn += num

    return rtn


def solve2():
    file = open("AoC3.txt", "r")
    lines = [line.strip() for line in file.readlines()]
    rtn = 0

    list = []
    for line in lines:
        row = []
        for char in line:
            row.append(char)
        list.append(row)

    rows = len(list)
    cols = len(list[0])

    gears = []

    for i in range(0, rows):
        for j in range(0, cols):
            if list[i][j] == '*':
                gears.append([i, j])

    for gear in gears:
        adjacent = set()

        row = gear[0]
        col = gear[1]

        adjacent.add(getNumber(list, row - 1, col - 1, rows, cols))
        adjacent.add(getNumber(list, row - 1, col, rows, cols))
        adjacent.add(getNumber(list, row - 1, col + 1, rows, cols))
        adjacent.add(getNumber(list, row, col - 1, rows, cols))
        adjacent.add(getNumber(list, row, col + 1, rows, cols))
        adjacent.add(getNumber(list, row + 1, col - 1, rows, cols))
        adjacent.add(getNumber(list, row + 1, col, rows, cols))
        adjacent.add(getNumber(list, row + 1, col + 1, rows, cols))

        adjacent = set(filter(lambda item: item is not None, adjacent))

        ratio = 1
        if len(adjacent) == 2:
            for num in adjacent:
                ratio *= num
            rtn += ratio

    return rtn


def getNumber(arr, row, col, rows, cols):
    if row < 0 or row >= rows or not arr[row][col].isdigit():
        return None

    num = []
    pos = col + 1
    while col > 0:
        if arr[row][col].isdigit():
            num.insert(0, int(arr[row][col]))
        else:
            break
        col -= 1

    while pos < cols:
        if arr[row][pos].isdigit():
            num.append(int(arr[row][pos]))
        else:
            break
        pos += 1

    mult = 1
    rtn = 0
    for digit in reversed(num):
        rtn += digit * mult
        mult *= 10

    return rtn

