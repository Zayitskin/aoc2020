
def load(path: str) -> list:
    """Load the input from a file."""
    data: list = []
    with open(path) as f:
        return [line.strip() for line in f]

def runASM(ticket: list[str], pc: int, acc: int) -> [int, int]:
    """Run the ASM code from ticket at pc and maintain the state of acc."""
    #NOP: do nothing, increment PC
    if ticket[pc].startswith("nop"):
        pc += 1
    #ACC: add value to ACC, increment PC
    elif ticket[pc].startswith("acc"):
        acc += int(data[pc].split(" ")[1])
        pc += 1
    #JMP add value to PC, but if zero, increment PC
    elif ticket[pc].startswith("jmp"):
        if int(data[pc].split(" ")[1]) != 0:
            pc += int(data[pc].split(" ")[1])
        else:
            pc += 1

    return pc, acc

def part1(data: list) -> int:

    #Instantiate the program counter, accumulator and list of visited pc's
    pc: int = 0
    acc: int = 0
    visited: list[int] = []

    #Continuously run the ASM code
    while True:
        #If a particular call has been called before, an infinite loop has
        #happened, so the ACC has the solution
        if pc in visited:
            break

        #Add the PC to the list so that infinite loops can be identifies
        visited.append(pc)

        #Run the ASM and update the PC and ACC
        pc, acc = runASM(data, pc, acc)

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
