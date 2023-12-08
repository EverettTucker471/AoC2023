import math


def solve1():
    file = open("AoC8.txt", "r")
    lines = [line.strip() for line in file.readlines()]

    pattern = lines[0]

    graph = {}
    for line in lines:
        index = line.find('=')
        if index >= 0:
            begin, end = line.split('=')
            graph[begin.strip()] = end.strip().strip("(").strip(")").split(", ")

    rtn = 0
    n = len(pattern)
    cur = 'AAA'
    while cur != 'ZZZ':
        if pattern[rtn % n] == 'L':
            cur = graph[cur][0]
        else:
            cur = graph[cur][1]
        rtn += 1

    return rtn


def solve2():
    file = open("AoC8.txt", "r")
    lines = [line.strip() for line in file.readlines()]

    pattern = lines[0]

    graph = {}
    for line in lines:
        index = line.find('=')
        if index >= 0:
            begin, end = line.split('=')
            graph[begin.strip()] = end.strip().strip("(").strip(")").split(", ")

    starting = []
    for key in graph.keys():
        if key[2] == 'A':
            starting.append(key)

    steps = []
    n = len(pattern)
    for start in starting:
        iterations = 0
        while start[2] != 'Z':
            if pattern[iterations % n] == 'L':
                start = graph[start][0]
            else:
                start = graph[start][1]
            iterations += 1
        steps.append(iterations)

    rtn = 1
    for i in range(0, len(steps)):
        rtn = math.lcm(rtn, steps[i])
    return rtn
