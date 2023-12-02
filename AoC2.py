def solve1():
    file = open("AoC2.txt", "r")
    lines = [line.strip() for line in file.readlines()]

    rtn = 0
    for i in range(0, len(lines)):
        lines[i] = lines[i][lines[i].find(':')+2:]
        sets = lines[i].split(';')

        num_red = 0
        num_blue = 0
        num_green = 0

        for group in sets:
            colors = [string.strip() for string in group.split(",")]
            for color in colors:
                if color.find("red") > -1:
                    num_red = max(num_red, int(color.strip(" red")))
                elif color.find("blue") > -1:
                    num_blue = max(num_blue, int(color.strip(" blue")))
                elif color.find("green") > -1:
                    num_green = max(num_green, int(color.strip(" green")))

        if num_blue <= 14 and num_green <= 13 and num_red <= 12:
            rtn += i + 1

    return rtn


def solve2():
    file = open("AoC2.txt", "r")
    lines = [line.strip() for line in file.readlines()]

    rtn = 0
    for i in range(0, len(lines)):
        lines[i] = lines[i][lines[i].find(':') + 2:]
        sets = lines[i].split(';')

        num_red = 0
        num_blue = 0
        num_green = 0

        for group in sets:
            colors = [string.strip() for string in group.split(",")]
            for color in colors:
                if color.find("red") > -1:
                    num_red = max(num_red, int(color.strip(" red")))
                elif color.find("blue") > -1:
                    num_blue = max(num_blue, int(color.strip(" blue")))
                elif color.find("green") > -1:
                    num_green = max(num_green, int(color.strip(" green")))

        power = num_red * num_green * num_blue
        rtn += power

    return rtn