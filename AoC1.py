def solve1():
    file = open("AoC1.txt")
    lines = [line.strip() for line in file.readlines()]

    rtn = 0
    for line in lines:
        left_digit = 0
        right_digit = 0
        n = len(line)

        for i in range(0, n):
            if line[i].isdigit():
                left_digit = int(line[i])
                break

        j = n - 1
        while j >= 0:
            if line[j].isdigit():
                right_digit = int(line[j])
                break
            j -= 1

        rtn += 10 * left_digit + right_digit

    return rtn

def solve1ALT():
    file = open("AoC1.txt")
    lines = [line.strip() for line in file.readlines()]

    rtn = 0
    for line in lines:
        for char in line:
            if char.isdigit():
                rtn += 10 * int(char)
                break

        for char in reversed(line):
            if char.isdigit():
                rtn += int(char)
                break

    return rtn


"""
I had to change up the approach for the second problem.
This is a simpler approach that makes use of the Python find and rfind functions.
"""
def solve2():
    file = open("AoC1.txt")
    lines = [line.strip() for line in file.readlines()]
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    rtn = 0
    for line in lines:
        n = len(line)
        left_digit = 0
        right_digit = 0

        left_index = n
        right_index = -1

        for i in range(9):
            if -1 < line.find(words[i]) < left_index:
                left_digit = i + 1
                left_index = line.find(words[i])
            if -1 < line.find(digits[i]) < left_index:
                left_digit = i + 1
                left_index = line.find(digits[i])

        for i in range(9):
            if line.rfind(words[i]) > right_index:
                right_digit = i + 1
                right_index = line.rfind(words[i])
            if line.rfind(digits[i]) > right_index:
                right_digit = i + 1
                right_index = line.rfind(digits[i])

        rtn += 10 * left_digit + right_digit

    return rtn