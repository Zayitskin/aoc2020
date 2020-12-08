
def load(path: str) -> list:

    data: list = []
    with open(path) as f:
        return [line.strip() for line in f]

def part1(data: list) -> int:

    pc: int = 0
    acc: int = 0
    visited: list[int] = []
    while True:
        if pc in visited:
            break
        
        visited.append(pc)

        if data[pc].startswith("nop"):
            pc += 1
        elif data[pc].startswith("acc"):
            acc += int(data[pc].split(" ")[1])
            pc += 1
        elif data[pc].startswith("jmp"):
            pc += int(data[pc].split(" ")[1])

    return acc

def part2(data: list) -> int:

    
    
    potentials: list = []

    for call in range(len(data)):
        if not data[call].startswith("acc"):
            potentials.append(call)

    for potential in potentials:
        pc: int = 0
        acc: int = 0
        visited: list[int] = []

        while True:
            if pc in visited:
                break
            elif pc == len(data):
                return acc
            visited.append(pc)
            
            if data[pc].startswith("nop"):
                if pc != potential:
                    pc += 1
                else:
                    pc += int(data[pc].split(" ")[1])
            elif data[pc].startswith("acc"):
                acc += int(data[pc].split(" ")[1])
                pc += 1
            elif data[pc].startswith("jmp"):
                if pc != potential:
                    pc += int(data[pc].split(" ")[1])
                else:
                    pc += 1
        

if __name__ == "__main__":

    data: list = load("opcodes.txt")
    print(f"Part 1: {part1(data)}\nPart 2: {part2(data)}")
