import math

# ANS: 76350869 <-- Wrong Greater than this
# ANS: 33942461 <-- Wrong
# ANS: 176264891 <-- Wrong
# ANS: 61779304 <-- Wrong
# ANS: 316110251 <-- Wrong
# New? 136096660 Correct!


def solve1():
    file = open("AoC5.txt", "r")
    lines = [line.strip() for line in file.readlines()]

    seeds = [int(num) for num in lines[0][6:].strip().split(' ')]

    maps = []
    map = {}
    for line in lines:
        if line == '':
            maps.append(map)
        elif line.find(':') >= 0:
            map = {}
        else:
            nums = [int(num) for num in line.strip().split(' ')]
            map[nums[0]] = [nums[1], nums[1] + nums[2] - 1]
    maps.append(map)
    maps.pop(0)

    locations = []
    for seed in seeds:
        for map in maps:
            for key in map.keys():
                if map[key][0] <= seed <= map[key][1]:
                    seed = key + seed - map[key][0]
                    break
        locations.append(seed)

    return min(locations)


"""
Brute force solution is not possible. I will need something more creative.

Idea:
Attempt to merge the maps into one single map, then finding minimum should be easy

Idea:
Run it backwards and then see if that number is in the final seeds intervals O(ANS) --> O(10^10) (too much)
This could potentially work if I just leave it for a while

Idea:
Compute the maximum drop through all interval paths
 --> theoretically about 10^9 paths, but probably about 2^7 times less in practice, which is feasible.
 
Winning Idea:
Compute it using intervals, instead of actual values.
Then compute the minimum value in any of those intervals.
"""


def solve2():
    file = open("AoC5.txt", "r")
    lines = [line.strip() for line in file.readlines()]

    seeds = [int(num) for num in lines[0][6:].strip().split(' ')]

    intervals = []
    for i in range(0, int(len(seeds) / 2)):
        intervals.append([seeds[2 * i], seeds[2 * i] + seeds[2 * i + 1] - 1])

    maps = []
    modifier = []
    for line in lines:
        if line == '':
            maps.append(modifier)
        elif line.find(':') >= 0:
            modifier = []
        else:
            nums = [int(num) for num in line.strip().split(' ')]
            modifier.append((nums[0] - nums[1], [nums[1], nums[1] + nums[2] - 1]))
    maps.append(modifier)
    maps.pop(0)

    for map in maps:
        next_intervals = []
        for interval in intervals:
            union = [interval]
            for val in map:
                next_union = []
                for tuple in union:
                    left = [tuple[0], min(val[1][0] - 1, tuple[1])]
                    middle = [max(tuple[0], val[1][0]) + val[0], min(tuple[1], val[1][1]) + val[0]]
                    right = [max(val[1][1] + 1, tuple[0]), tuple[1]]

                    if left[1] >= left[0]:
                        next_union.append(left)
                    if middle[1] >= middle[0]:
                        next_intervals.append(middle)
                    if right[1] >= right[0]:
                        next_union.append(right)

                union = next_union

            next_intervals.extend(union)

        intervals = next_intervals

    rtn = math.inf
    for interval in intervals:
        rtn = min(rtn, interval[0])

    return rtn
