import functools

rankings = {'A': 1,
            'K': 2,
            'Q': 3,
            'T': 5,
            '9': 6,
            '8': 7,
            '7': 8,
            '6': 9,
            '5': 10,
            '4': 11,
            '3': 12,
            '2': 13,
            'J': 14}


def solve2():
    file = open("AoC7.txt", "r")
    lines = [line.strip() for line in file.readlines()]

    hands = []
    for line in lines:
        card, bid = line.split(' ')
        hands.append((card, int(bid)))

    hands = sorted(hands, key=functools.cmp_to_key(compare))

    rtn = 0
    for i in range(0, len(hands)):
        rtn += hands[i][1] * (i + 1)

    return rtn


def computeType(card):
    characters = {}
    num_jokers = 0
    for letter in card:
        if letter == 'J':
            num_jokers += 1
        else:
            characters[letter] = characters.get(letter, 0) + 1

    frequencies = {}
    for frequency in characters.values():
        frequencies[frequency] = frequencies.get(frequency, 0) + 1

    if num_jokers == 5:
        return 0  # 5 of a kind
    if max(frequencies.keys()) + num_jokers == 5:
        return 0  # 5 of a kind
    elif max(frequencies.keys()) + num_jokers == 4:
        return 1  # 4 of a kind
    if max(frequencies.keys()) + num_jokers == 3:  # At this point, we have necessarily used all our jokers
        if num_jokers == 2:
            return 3  # 3 of a kind
        elif num_jokers == 1:
            if frequencies.get(2, 0) == 2:
                return 2  # Full House
            else:
                return 3  # 3 of a kind
        else:
            if frequencies.get(2, 0) > 0:
                return 2  # Full House
            else:
                return 3  # 3 of a kind
    if max(frequencies.keys()) + num_jokers == 2:
        if num_jokers == 1:
            return 5  # 1 pair
        else:
            if frequencies.get(2, 0) > 1:
                return 4  # 2 pairs
            else:
                return 5  # 1 pair
    return 6  # Nothing


def compare(self, other):
    self_type = computeType(self[0])
    other_type = computeType(other[0])
    if self_type < other_type:
        return 1
    elif self_type > other_type:
        return -1
    else:
        for i in range(0, 5):
            if rankings[self[0][i]] != rankings[other[0][i]]:
                if rankings[self[0][i]] < rankings[other[0][i]]:
                    return 1
                else:
                    return -1
    return 0
