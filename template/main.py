
def load(path: str) -> list:

    data: list = []
    with open(path) as f:
        return [line.strip() for line in f]

def part1(data: list) -> int:

    return 0

def part2(data: list) -> int:

    return 0

if __name__ == "__main__":

    data = load(".txt")
    print(f"Part 1: {part1(data)}\nPart 2: {part2(data)}")
