from Stacker import Stacker


def solve1():
    file = open("AoC4.txt", "r")
    lines = [line.strip() for line in file.readlines()]

    rtn = 0
    for line in lines:
        num_lucky = 0
        line = line[line.find(':') + 1:].strip()
        left, right = line.split('|')
        left = [int(num) for num in left.strip().split(' ') if num != '']
        right = [int(num.strip()) for num in right.strip().split(' ') if num != '']

        for num in left:
            if num in right:
                num_lucky += 1
        if num_lucky > 0:
            rtn += 2 ** (num_lucky - 1)
    return rtn


# This one actually took a while to run, about 10 seconds
def solve2():
    file = open("AoC4.txt", "r")
    lines = [line.strip() for line in file.readlines()]

    # We need more preprocessing
    arr = []
    stack = Stacker()
    for line in lines:
        line = line[line.find(':') + 1:].strip()
        left, right = line.split('|')
        left = [int(num) for num in left.strip().split(' ') if num != '']
        right = [int(num.strip()) for num in right.strip().split(' ') if num != '']

        lucky = 0
        for num in left:
            if num in right:
                lucky += 1
        arr.append(lucky)

    """
    One could probably use a dynamic programming based approach to speed this up, 
    but it is too early to worry about that.
    """
    rtn = 0
    for i in range(0, len(arr)):
        stack.push(i)

    while not stack.isEmpty():
        rtn += 1
        index = stack.pop()
        lucky = arr[index]

        for i in range(index + 1, index + lucky + 1):
            stack.push(i)

    return rtn


"""
This is the aforementioned dynamic programming approach.
The other code takes about 7 seconds to run, this takes only 2 milliseconds
"""
def solve2Fast():
    file = open("AoC4.txt", "r")
    lines = [line.strip() for line in file.readlines()]

    # We need more preprocessing
    arr = []
    for line in lines:
        line = line[line.find(':') + 1:].strip()
        left, right = line.split('|')
        left = [int(num) for num in left.strip().split(' ') if num != '']
        right = [int(num.strip()) for num in right.strip().split(' ') if num != '']

        lucky = 0
        for num in left:
            if num in right:
                lucky += 1
        arr.append(lucky)

    map = {}
    for i in reversed(range(0, len(arr))):
        val = 1
        for j in range(i+1, i+arr[i]+1):
            val += map.get(j, 0)
        map[i] = val

    return sum(map.values())
