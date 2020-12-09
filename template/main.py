
def load(path: str) -> list:
    """Load the input from a file."""
    data: list = []
    with open(path) as f:
        return [line.strip() for line in f]

def part1(data: list) -> int:

    return 0

def part2(data: list) -> int:

    return 0

if __name__ == "__main__":

    #Load the input data
    data: list = load(".txt")
    #Print the answers for part 1 and 2
    print(f"Part 1: {part1(data)}\nPart 2: {part2(data)}")
