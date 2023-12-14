def solve1():
    # ANS: 33356
    file = open("AoC13.txt", "r")
    lines = [line.strip() for line in file.readlines()]

    cases = []
    temp = []
    for line in lines:
        if line == '':
            cases.append(temp)
            temp = []
        else:
            row = []
            for char in line:
                row.append(char)
            temp.append(row)
    cases.append(temp)

    rtn = 0
    for case in cases:
        # Generate row cases and column cases
        row_case = []
        col_case = []

        n = len(case)
        m = len(case[0])

        for i in range(0, n):
            temp = ""
            for j in range(0, m):
                temp += case[i][j]
            row_case.append(temp)

        for j in range(0, m):
            temp = ""
            for i in range(0, n):
                temp += case[i][j]
            col_case.append(temp)

        # There is only ever one line of symmetry for any input table
        # Finding horizontal symmetries
        horizontal = 0
        for i in range(1, n):
            flag = True
            for j in range(0, i):
                if 2 * i - j - 1 < n and row_case[j] != row_case[2 * i - j - 1]:
                    flag = False
                    break
            if flag:
                horizontal += i
                break

        # Finding the vertical symmetries
        vertical = 0
        for i in range(1, m):
            flag = True
            for j in range(0, i):
                if 2 * i - j - 1 < m and col_case[j] != col_case[2 * i - j - 1]:
                    flag = False
                    break
            if flag:
                vertical += i
                break

        rtn += 100 * horizontal + vertical

    return rtn

"""
Compute an off-ness score for each pattern, the number of characters that are off
Then, we are just looking for the reflection with an off-ness score of 1
"""


def solve2():
    file = open("AoC13.txt", "r")
    lines = [line.strip() for line in file.readlines()]

    cases = []
    temp = []
    for line in lines:
        if line == '':
            cases.append(temp)
            temp = []
        else:
            row = []
            for char in line:
                row.append(char)
            temp.append(row)
    cases.append(temp)

    rtn = 0
    for case in cases:
        # Generate row cases and column cases
        row_case = []
        col_case = []

        n = len(case)
        m = len(case[0])

        for i in range(0, n):
            temp = ""
            for j in range(0, m):
                temp += case[i][j]
            row_case.append(temp)

        for j in range(0, m):
            temp = ""
            for i in range(0, n):
                temp += case[i][j]
            col_case.append(temp)

        horizontal = 0
        for i in range(1, n):
            error = 0
            for j in range(0, i):
                if 2 * i - j - 1 < n:
                    for k in range(0, m):
                        if row_case[j][k] != row_case[2 * i - j - 1][k]:
                            error += 1
                if error > 1:
                    break
            if error == 1:
                horizontal += i

        # Finding the vertical symmetries
        vertical = 0
        for i in range(1, m):
            error = 0
            for j in range(0, i):
                if 2 * i - j - 1 < m:
                    for k in range(0, n):
                        if col_case[j][k] != col_case[2 * i - j - 1][k]:
                            error += 1
                if error > 1:
                    break
            if error == 1:
                vertical += i

        rtn += 100 * horizontal + vertical

    return rtn
