
def load(path: str) -> list[int]:
    """Load the input from a file."""
    data: list = []
    with open(path) as f:
        return [int(line.strip()) for line in f]

def part1(data: list[int]) -> int:

    #Find the two different numbers that add to 2020 and multiply them
    for i in range(len(data)):
        for j in range(len(data)):
            if i == j:
                continue

            if data[i] + data[j] == 2020:
                return data[i] * data[j]

def part2(data: list[int]) -> int:

    #Find the three different numbers that add to 2020 and multiply them
    for i in range(len(data)):
        for j in range(len(data)):
            for k in range(len(data)):
                if i == j or i == k or j == k:
                    continue

                if data[i] + data[j] + data[k] == 2020:
                    return data[i] * data[j] * data[k]
                

if __name__ == "__main__":

    #Load the input data
    data: list[int] = load("expenses.txt")
    #Print the answers for part 1 and 2
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")

    
