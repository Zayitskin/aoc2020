
def load(path: str) -> list:
    """Load the input from a file."""
    data: list = []
    with open(path) as f:
        return [line.strip() for line in f]

def part1(data: list) -> int:

    greatest: int = 0

    #For each row in data, convert to binary and set greatest to max of both
    for tick in data:
        row: str = tick[:7]
        row = row.replace("B", "1")
        row = row.replace("F", "0")
        col: str = tick[7:]
        col = col.replace("R", "1")
        col = col.replace("L", "0")
        if int(row, 2) * 8 + int(col, 2) > greatest:
            greatest = int(row, 2) * 8 + int(col, 2)
        
    return greatest

def part2(data: list) -> int:

    ids: list = []

    #Store all of the ids from the binary representation into ids
    for tick in data:
        row: str = tick[:7]
        row = row.replace("B", "1")
        row = row.replace("F", "0")
        col: str = tick[7:]
        col = col.replace("R", "1")
        col = col.replace("L", "0")
        ids.append(int(row, 2) * 8 + int(col, 2))
    #Sort them numerically
    ids.sort()
    #Find the one for which the previous is more than one less and return it
    last: int = ids[0]
    for _id in range(1, len(ids)):
        if ids[_id] - last != 1:
            return ids[_id] - 1
        else:
            last = ids[_id]
        
    return -1

if __name__ == "__main__":

    #Load the input data
    data: list = load("passes.txt")
    #Print the answers for part 1 and 2
    print(f"Part 1: {part1(data)}\nPart 2: {part2(data)}")
