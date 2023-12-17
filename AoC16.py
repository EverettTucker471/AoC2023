def solve1():
    file = open("AoC16.txt", "r")
    lines = [line.strip() for line in file.readlines()]

    # As a note, the '\' character is actually '\\'
    grid = []
    for line in lines:
        grid.append(list(line))

    """
    The tolerance measures how many times you permit the cycle to run without
    any new coordinates being added to the explored set
    The first part takes a tolerance of 16 to find the right answer,
    but I would suggest running it with a higher tolerance of about 1000, just to be sure
    The coordinates listed below are initial coordinates, for part 2
    """
    tolerance = 1000
    return compute(grid, tolerance, 0, 0, 1, 0)


def solve2():
    file = open("AoC16.txt", "r")
    lines = [line.strip() for line in file.readlines()]

    # As a note, the '\' character is actually '\\'
    grid = []
    for line in lines:
        grid.append(list(line))

    n = len(grid)  # The grid is square
    tolerance = 1000
    rtn = 0

    # Top
    for i in range(0, n):
        rtn = max(rtn, compute(grid, tolerance, i, 0, 0, 1))

    # Left
    for i in range(0, n):
        rtn = max(rtn, compute(grid, tolerance, 0, i, 1, 0))

    # Bottom
    for i in range(0, n):
        rtn = max(rtn, compute(grid, tolerance, i, n - 1, 0, -1))

    # Right
    for i in range(0, n):
        rtn = max(rtn, compute(grid, tolerance, n - 1, i, -1, 0))

    return rtn


def compute(grid, tolerance, pos_x, pos_y, vel_x, vel_y):
    n = len(grid)  # The grid is square
    beams = [Beam(pos_x, pos_y, vel_x, vel_y)]
    beam_hashes = set()
    explored = set()
    while tolerance > 0:
        prev_size = len(explored)
        next_beams = []
        while len(beams) > 0:
            beam = beams.pop(0)  # Assume that the beam is within the grid
            explored.add(beam.pos_x + n * beam.pos_y)
            beam_hashes.add(beam.hash(n))
            beam.move()
            if 0 <= beam.pos_x < n and 0 <= beam.pos_y < n:
                char = grid[beam.pos_y][beam.pos_x]
                if char == '-':
                    if beam.vel_x == 0:
                        if beam.pos_x - 1 >= 0:
                            addWRTHash(next_beams, beam_hashes, Beam(beam.pos_x, beam.pos_y, -1, 0), n)
                        if beam.pos_x + 1 < n:
                            addWRTHash(next_beams, beam_hashes, Beam(beam.pos_x, beam.pos_y, 1, 0), n)
                    else:
                        addWRTHash(next_beams, beam_hashes, beam, n)
                elif char == '|':
                    if beam.vel_y == 0:
                        if beam.pos_y - 1 >= 0:
                            addWRTHash(next_beams, beam_hashes, Beam(beam.pos_x, beam.pos_y, 0, -1), n)
                        if beam.pos_y + 1 < n:
                            addWRTHash(next_beams, beam_hashes, Beam(beam.pos_x, beam.pos_y, 0, 1), n)
                    else:
                        addWRTHash(next_beams, beam_hashes, beam, n)
                else:
                    beam.alter(char)
                    addWRTHash(next_beams, beam_hashes, beam, n)

        beams = next_beams
        if len(explored) == prev_size:
            tolerance -= 1

    return len(explored)


def addWRTHash(arr, hashes, beam, n):
    if beam.hash(n) not in hashes:
        arr.append(beam)


class Beam:
    def __init__(self, pos_x, pos_y, vel_x, vel_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = vel_x
        self.vel_y = vel_y

    def move(self):
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y

    def alter(self, char):
        if char == '\\':
            if self.vel_x == 1:
                self.vel_y = 1
                self.vel_x = 0
            elif self.vel_x == -1:
                self.vel_x = 0
                self.vel_y = -1
            elif self.vel_y == 1:
                self.vel_x = 1
                self.vel_y = 0
            elif self.vel_y == -1:
                self.vel_x = -1
                self.vel_y = 0
        elif char == '/':
            if self.vel_x == 1:
                self.vel_y = -1
                self.vel_x = 0
            elif self.vel_x == -1:
                self.vel_x = 0
                self.vel_y = 1
            elif self.vel_y == 1:
                self.vel_x = -1
                self.vel_y = 0
            elif self.vel_y == -1:
                self.vel_x = 1
                self.vel_y = 0

    def hash(self, n):
        if self.vel_x == 1:
            modifier = 1
        elif self.vel_x == -1:
            modifier = 2
        elif self.vel_y == 1:
            modifier = 3
        else:
            modifier = 4
        return self.pos_x + n * self.pos_y + n ** 2 * modifier
