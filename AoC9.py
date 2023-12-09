def solve1():
    file = open("AoC9.txt", "r")
    lines = [line.strip() for line in file.readlines()]

    data = []
    for line in lines:
        data.append([int(num) for num in line.split(' ')])

    """
        The next value is the sum of all the partial differences
    """

    rtn = 0
    for pattern in data:
        next_value = 0
        while not isAllZero(pattern):
            next_value += pattern[-1]
            pattern = computeDiff(pattern)
        rtn += next_value

    return rtn


def computeDiff(arr):
    rtn = []
    for i in range(0, len(arr) - 1):
        rtn.append(arr[i + 1] - arr[i])
    return rtn


def isAllZero(arr):
    for num in arr:
        if num != 0:
            return False
    return True


def solve2():
    file = open("AoC9.txt", "r")
    lines = [line.strip() for line in file.readlines()]

    data = []
    for line in lines:
        data.append([int(num) for num in line.split(' ')])

    """
    The next value is the alternating sum of the first row of differences
    """

    rtn = 0
    for pattern in data:
        next_value = 0
        flag = True
        while not isAllZero(pattern):
            if flag:
                next_value += pattern[0]
                flag = False
            else:
                next_value -= pattern[0]
                flag = True
            pattern = computeDiff(pattern)

        rtn += next_value

    return rtn
