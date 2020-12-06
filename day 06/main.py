from collections import Counter

def load(path: str) -> list:

    data: list = []
    with open(path) as f:
        return [line.strip() for line in f]

def groupSet(data: list) -> list[set]:

    s: set = set()
    sets: list = []
    for line in data:
        if line == "":
            sets.append(s)
            s = set()
        else:
            for bit in line:
                s.add(bit)

    if len(s) > 0:
        sets.append(s)
    return sets
    
def groupList(data: list) -> list:

    rl: list = []
    tl: list = []
    for line in data:
        if line == "":
            rl.append(tl)
            tl = []
        else:
            tl.append(line)

    if len(tl) > 0:
        rl.append(tl)
    return rl

def part1(data: list) -> int:

    count: int = 0
    for s in data:
        count += len(s)
    return count

def part2(data: list) -> int:

    count: int = 0

    for group in data:
        counter: Counter = Counter()
        for member in group:
            counter.update(member)
        for ele in counter:
            if counter[ele] == len(group):
                count += 1
        
    return count

if __name__ == "__main__":

    data: list = load("surveys.txt")
    sets: list[set] = groupSet(data)
    lists: list = groupList(data)
    print(f"Part 1: {part1(sets)}\nPart 2: {part2(lists)}")
