
def load(path: str) -> list:
    """Load the input from a file."""
    data: list = []
    with open(path) as f:
        return [int(line.strip()) for line in f]

def part1(data: list) -> int:

    start: int = 0
    end: int = 25
    #Go through each number in the list
    for i in range(25, len(data)):
        cleared: bool = False
        #For each pair of different numbers in the previous 25
        for x in range(start, end):
            for y in range(start, end):
                if x == y:
                    continue
                #Ensure at least one pair adds to the current number
                if data[i] == data[x] + data[y]:
                    cleared = True
        #If none does, the current number is the solution
        if cleared == False:
            return data[i]
        #Otherwise, shift forward the 25 numbers to be checked
        else:
            start += 1
            end += 1
            
    return -1

def part2(data: list) -> int:

    #Good ol' hardcoded solution to part 1
    target: int = 257342611

    #For each number in the input
    for i in range(len(data)):
        total: int = 0
        j: int = i - 1
        #TODO: replace with something guarenteed for small < any possible input
        small: int = 9999999999999999999999999999999999999
        large: int = 0
        #Go through numbers until the total is not less than the target
        while total < target:
            j += 1
            total += data[j]
            #While doing this, remember the smallest and largest numbers seen
            if data[j] < small:
                small = data[j]
            if data[j] > large:
                large = data[j]
        #If it happens to exactly match the total, return the sum of
        #the largest and smallest number that was added to the total
        if total == target:
            return small + large
            
    return -1

if __name__ == "__main__":

    #Load the input data
    data: list = load("numbers.txt")
    #Print the answers for part 1 and 2
    print(f"Part 1: {part1(data)}\nPart 2: {part2(data)}")
