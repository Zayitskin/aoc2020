from functools import cache

def load(path: str) -> list:
    """Load the input from a file."""
    data: list = []
    with open(path) as f:
        return [int(line.strip()) for line in f]

@cache
def countWays(data: tuple) -> int:
    """Recursively count the paths with memoization to improve speed."""
    #The base condition for the recursive function
    if len(data) == 1:
        return 1
        
    ways: int = 0
    #The number of ways from a location is equal to the sum of the ways
    #from all locations that are no more than three more than the current
    #location (assuming that it is not the base case)
    for i in range(1, len(data)):
        if data[i] - data[0] <= 3:
            ways += countWays(data[i:])

    return ways

def part1(data: list) -> int:

    ones: int = 0
    threes: int = 1
    previous: int = 0

    #For each adapter, count the number of adapters that are exactly one or
    #three more than it, and then set the previous to the current adapter
    for adapter in data:
        if adapter - previous == 1:
            ones += 1
        elif adapter - previous == 3:
            threes += 1
        previous = adapter
    #Return the product of the counted ones and threes
    return ones * threes

def part2(data: tuple) -> int:

    #Count the total number of ways
    return countWays(data)

if __name__ == "__main__":

    #Load the input data, sort it, and add the base condition
    data: list = load("adapters.txt")
    data.sort()
    data.insert(0, 0)
    #In order to support caching, the data needs to be hashable
    hashableData = tuple(data)
    print(hashableData)
    #Print the answers for part 1 and 2
    print(f"Part 1: {part1(data)}\nPart 2: {part2(hashableData)}")
