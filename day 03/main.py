
def load(path: str) -> list:
    """Load the input from a file."""
    data: list = []
    with open(path) as f:
        return [line.strip() for line in f]

def part1(data: list, run: int, fall: int) -> int:

    width: int = len(data[0])
    x: int = 0
    y: int = 0
    hits: int = 0

    #Count the number of trees hit with a given slope
    while y < len(data) - 1:
        x += run
        if x >= width:
            x -= width
        y += fall
        if data[y][x] == "#":
            hits += 1

    return hits

def part2(data: list) -> int:

    #Add up all of the trees hit with given slopes
    a: int = part1(data, 1, 1)
    b: int = part1(data, 3, 1)
    c: int = part1(data, 5, 1)
    d: int = part1(data, 7, 1)
    e: int = part1(data, 1, 2)

    return a * b * c * d * e

if __name__ == "__main__":

    #Load the input data
    data: list = load("field.txt")
    #Print the answers for part 1 and 2
    print(f"Part 1: {part1(data, 3, 1)}\nPart 2: {part2(data)}")
