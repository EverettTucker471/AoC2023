def solve2():
    file = open("AoC10.txt", "r")
    lines = [line.strip() for line in file.readlines()]

    grid = []
    n = len(lines)
    for line in lines:
        for char in line:
            grid.append(char)

    start = 0
    for i in range(0, n ** 2):
        if grid[i] == 'S':
            start = i

    cur = 0
    orientation = 0
    if start in getAdjacent(grid, start - n, n):
        cur = start - n
        orientation = -1
    elif start in getAdjacent(grid, start + 1, n):
        cur = start + 1
        orientation = -n
    elif start in getAdjacent(grid, start - 1, n):
        cur = start - 1
        orientation = n
    elif start in getAdjacent(grid, start + n, n):
        cur = start + n
        orientation = 1

    prev = start
    loop = [start]
    loop_set = set()
    loop_set.add(start)
    while cur != start:
        loop.append(cur)
        loop_set.add(cur)
        for node in getAdjacent(grid, cur, n):
            if node != prev:
                prev = cur
                cur = node
                break

    # This is assumed to be a clockwise traversal with the inside on the left.
    # It matches current direction with where the inside of the curve is
    orientation_map = {1: -n, -1: n, n: 1, -n: -1}
    bfs_queue = []

    k = len(loop)
    for i in range(0, k):
        cur = loop[i]
        next = loop[(i + 1) % k]

        # Adding an item to the bfs_queue
        if cur + orientation not in loop_set:
            bfs_queue.append(cur + orientation)

        # Changing the orientation
        if grid[cur] == '7':
            if next == cur + n:
                orientation = orientation_map[n]
            else:
                orientation = orientation_map[-1]
        elif grid[cur] == 'J':
            if next == cur - n:
                orientation = orientation_map[-n]
            else:
                orientation = orientation_map[-1]
        elif grid[cur] == 'L':
            if next == cur - n:
                orientation = orientation_map[-n]
            else:
                orientation = orientation_map[1]
        elif grid[cur] == 'F':
            if next == cur + n:
                orientation = orientation_map[n]
            else:
                orientation = orientation_map[1]

        # Checking orientation after switched for security
        if cur + orientation not in loop_set:
            bfs_queue.append(cur + orientation)

    explored = set()
    while len(bfs_queue) != 0:
        vertex = bfs_queue.pop(0)
        if vertex not in explored:
            explored.add(vertex)
            if vertex + n not in explored and vertex + n not in loop_set:
                bfs_queue.append(vertex + n)
            if vertex - n not in explored and vertex - n not in loop_set:
                bfs_queue.append(vertex - n)
            if vertex + 1 not in explored and vertex + 1 not in loop_set:
                bfs_queue.append(vertex + 1)
            if vertex - n not in explored and vertex - n not in loop_set:
                bfs_queue.append(vertex - n)

    return len(explored)


def getAdjacent(grid, index, n):
    char = grid[index]
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
