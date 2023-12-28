import re


def solve1ALT():
    """
    The eval function is cursed with errors.
    :return:
    """
    file = open("AoC19.txt", "r")
    lines = [line.strip() for line in file.readlines()]

    # This will be a map of strings to lambda expressions
    workflows = {}
    parts = []

    word_regex = re.compile(r'\w+')

    for line in lines:
        if word_regex.match(line):
            key = word_regex.findall(line)[0]
            workflows[key] = []
            for expression in line[len(key):].strip('{').strip('}').split(','):
                clauses = str(expression).split(':')
                if len(clauses) == 1:
                    string = str(clauses[0])
                    workflows[key].append(lambda x, m, a, s: str(string))
                elif len(clauses) == 2:
                    first = str(clauses[0])
                    second = str(clauses[1])
                    workflows[key].append(lambda x, m, a, s: str(second) if eval(str(first), {}, {'x': x, 'm': m, 'a': a, 's': s}) else None)
                clauses.clear()
        elif line != "":
            arguments = [int(a.split('=')[1]) for a in line.strip('{').strip('}').split(',')]
            parts.append(Part(arguments[0], arguments[1], arguments[2], arguments[3]))

    rtn = 0
    for part in parts:
        current = 'in'
        while True:
            if current == 'R':
                break
            elif current == 'A':
                rtn += part.computeSum()
                break
            else:
                for function in workflows[current]:
                    ans = function(part.x, part.m, part.a, part.s)
                    if ans is not None:
                        current = ans
                        break

    return rtn


def solve1():
    file = open("AoC19.txt", "r")
    lines = [line.strip() for line in file.readlines()]

    # This will be a map of strings to lists of Function objects
    workflows = {}
    parts = []

    word_regex = re.compile(r'\w+')

    for line in lines:
        if word_regex.match(line):
            key = word_regex.findall(line)[0]
            workflows[key] = []
            for expression in line[len(key):].strip('{').strip('}').split(','):
                clauses = str(expression).split(':')
                if len(clauses) == 1:
                    workflows[key].append(Function(None, None, None, clauses[0], True))
                else:
                    workflows[key].append(Function(clauses[0][0], clauses[0][1], int(clauses[0][2:]), clauses[1], False))
        elif line != "":
            arguments = [int(a.split('=')[1]) for a in line.strip('{').strip('}').split(',')]
            parts.append(Part(arguments[0], arguments[1], arguments[2], arguments[3]))

    rtn = 0
    for part in parts:
        current = 'in'
        while True:
            if current == 'R':
                break
            elif current == 'A':
                rtn += part.computeSum()
                break
            else:
                for function in workflows[current]:
                    ans = function.evaluate(part)
                    if ans is not None:
                        current = ans
                        break

    return rtn


def solve2():
    file = open("AoC19.txt", "r")
    lines = [line.strip() for line in file.readlines()]

    # This will be a map of strings to lists of Function objects
    workflows = {}
    word_regex = re.compile(r'\w+')

    for line in lines:
        if word_regex.match(line):
            key = word_regex.findall(line)[0]
            workflows[key] = []
            for expression in line[len(key):].strip('{').strip('}').split(','):
                clauses = str(expression).split(':')
                if len(clauses) == 1:
                    workflows[key].append(Function(None, None, None, clauses[0], True))
                else:
                    workflows[key].append(
                        Function(clauses[0][0], clauses[0][1], int(clauses[0][2:]), clauses[1], False))

    """
    We only have to consider one part, which is 4000^4 combinations
    This is far too many to test each case.
    Solution: Use a recursive approach that builds a list of conditions for accepted parts
    Each solution list is a list of Functions, and is built for each possibility in the workflow
    We have to have a way to negate Functions <-- Done
    """

    accepted_function_paths = findAcceptedPaths('in', [], workflows, [])

    rtn = 0
    for path in accepted_function_paths:
        intervals = Intervals()
        for function in path:
            intervals.adjust(function)
        rtn += intervals.computeRange()

    return rtn


def findAcceptedPaths(cur, path, workflows, afps):
    for function in workflows[cur]:
        if function.result == 'A':
            temp = path.copy()
            temp.append(function)
            afps.append(temp)
        elif function.result != 'R':
            function.negate()
            path.append(function)
            afps = findAcceptedPaths(function.result, path, workflows, afps)
    return afps


class Intervals:
    def __init__(self):
        self.x = [1, 4000]
        self.m = [1, 4000]
        self.a = [1, 4000]
        self.s = [1, 4000]

    def adjust(self, function):
        if function.constant:
            return
        else:
            if function.operator == '<':
                if function.variable == 'x':
                    if function.negated:
                        self.x[0] = function.cutoff
                    else:
                        self.x[1] = function.cutoff - 1
                elif function.variable == 'm':
                    if function.negated:
                        self.m[0] = function.cutoff
                    else:
                        self.m[1] = function.cutoff - 1
                elif function.variable == 'a':
                    if function.negated:
                        self.a[0] = function.cutoff
                    else:
                        self.a[1] = function.cutoff - 1
                elif function.variable == 's':
                    if function.negated:
                        self.s[0] = function.cutoff
                    else:
                        self.s[1] = function.cutoff - 1
            else:
                if function.variable == 'x':
                    if function.negated:
                        self.x[1] = function.cutoff
                    else:
                        self.x[0] = function.cutoff + 1
                elif function.variable == 'm':
                    if function.negated:
                        self.m[1] = function.cutoff
                    else:
                        self.m[0] = function.cutoff + 1
                elif function.variable == 'a':
                    if function.negated:
                        self.a[1] = function.cutoff
                    else:
                        self.a[0] = function.cutoff + 1
                elif function.variable == 's':
                    if function.negated:
                        self.s[1] = function.cutoff
                    else:
                        self.s[0] = function.cutoff + 1

    def computeRange(self):
        return max(0, max(0, self.x[1] - self.x[0]) * max(0, self.m[1] - self.m[0]) * max(0, self.a[1] - self.a[0]) * max(0, self.s[1] - self.s[0]))


class Part:
    def __init__(self, x, m, a, s):
        self.x = x
        self.m = m
        self.a = a
        self.s = s

    def computeSum(self):
        return self.x + self.m + self.a + self.s

    def toString(self):
        return str(self.x) + ", " + str(self.m) + ", " + str(self.a) + ", " + str(self.s)


class Function:
    def __init__(self, variable, operator, cutoff, result, constant):
        self.variable = variable
        self.operator = operator
        self.cutoff = cutoff
        self.result = result
        self.constant = constant
        self.negated = False

    def evaluate(self, part):
        if self.constant:
            return self.result
        else:
            if self.variable == 'x':
                quant = part.x
            elif self.variable == 'm':
                quant = part.m
            elif self.variable == 'a':
                quant = part.a
            else:
                quant = part.s

            if self.operator == '<':
                return self.result if quant < self.cutoff else None
            else:
                return self.result if quant > self.cutoff else None

    def negate(self):
        self.negated = True

    def toString(self):
        if self.constant:
            return str(self.result) + " always"
        else:
            return str(self.result) + ' if ' + str(self.variable) + str(self.operator) + str(self.cutoff)


