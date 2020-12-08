from collections import Counter

def load(path: str) -> list:
    """Load the input from a file."""
    data: list = []
    with open(path) as f:
        return [line.strip() for line in f]

def groupSet(data: list) -> list[set]:
    """Turn the input into a list of sets."""
    s: set = set()
    sets: list = []

    #For each line:
    for line in data:
        #If the line is empty, the current set is complete
        if line == "":
            sets.append(s)
            s = set()
        #Otherwise, continue adding to the current set
        else:
            for bit in line:
                s.add(bit)
    #Add the final set if the input did not end in an empty line
    if len(s) > 0:
        sets.append(s)
    return sets
    
def groupList(data: list) -> list[list]:
    """Turn the input into a list of lists."""
    rl: list = []
    tl: list = []
    #For each line:
    for line in data:
        #If the line is empty, the current list is complete
        if line == "":
            rl.append(tl)
            tl = []
        #Otherwise, continue adding to the current list
        else:
            tl.append(line)

    #Add the final list if the input did not end in an empty line
    if len(tl) > 0:
        rl.append(tl)
    return rl

def part1(data: list) -> int:

    #Count each unique member of the set and return it
    count: int = 0
    for s in data:
        count += len(s)
    return count

def part2(data: list) -> int:

    count: int = 0
    
    for group in data:
        #Add up each instance in the list
        counter: Counter = Counter()
        for member in group:
            counter.update(member)
        for ele in counter:
            #If they are equal to the length of the list, count them
            if counter[ele] == len(group):
                count += 1
        
    return count

if __name__ == "__main__":

    #Load the data and then turn it into a group of sets and lists
    data: list = load("surveys.txt")
    sets: list[set] = groupSet(data)
    lists: list = groupList(data)
    #Print the answers for part 1 and 2
    print(f"Part 1: {part1(sets)}\nPart 2: {part2(lists)}")
