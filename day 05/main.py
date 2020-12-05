
def load(path: str) -> list:

    data: list = []
    with open(path) as f:
        return [line.strip() for line in f]

def part1(data: list) -> int:

    greatest = 0

    for tick in data:
        row = tick[:7]
        row = row.replace("B", "1")
        row = row.replace("F", "0")
        col = tick[7:]
        col = col.replace("R", "1")
        col = col.replace("L", "0")
        if int(row, 2) * 8 + int(col, 2) > greatest:
            greatest = int(row, 2) * 8 + int(col, 2)
        

    return greatest

def part2(data: list) -> int:

    ids = []
    
    for tick in data:
        row = tick[:7]
        row = row.replace("B", "1")
        row = row.replace("F", "0")
        col = tick[7:]
        col = col.replace("R", "1")
        col = col.replace("L", "0")
        ids.append(int(row, 2) * 8 + int(col, 2))
    ids.sort()
    last = ids[0]
    for _id in range(1, len(ids)):
        if ids[_id] - last != 1:
            return ids[_id] - 1
        else:
            last = ids[_id]
        

    return -1

if __name__ == "__main__":

    data = load("passes.txt")
    print(f"Part 1: {part1(data)}\nPart 2: {part2(data)}")
