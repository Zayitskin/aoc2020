
def load(path: str) -> list:
    """Load the input from a file."""
    data: list = []
    with open(path) as f:
        return [line.strip() for line in f]

def advance(data: list) -> list:
    """Advance the Game of Life state one iteration."""

    #Create a new list to hold the advanced state
    newSeats: list = []
    #For each row...
    for y in range(len(data)):
        #Create a new string to hold the advanced row
        newRow: str = ""
        #For each character in the row...
        for x in range(len(data[0])):
            #If empty
            if data[y][x] == ".":
                #Add empty to row
                newRow += "."

            #If open seat...
            elif data[y][x] == "L":
                #Check each direction for occupied seats
                alone: bool = True
                for ay, ax in [[y - 1, x - 1],
                               [y - 1, x ],
                               [y - 1, x + 1],
                               [y, x - 1],
                               [y, x],
                               [y, x + 1],
                               [y + 1, x - 1],
                               [y + 1, x],
                               [y + 1, x + 1]]:
                    try:
                        if ay > -1 and ax > -1:
                            if data[ay][ax] == "#":
                                alone = False
                    except IndexError:
                        pass
                #If all are open, make it occupied
                if alone == True:
                    newRow += "#"
                #Otherwise, leave it open
                else:
                    newRow += "L"

            #If occupied seat...
            elif data[y][x] == "#":
                near: int = 0
                #Check each direction for occupied seats
                for ay, ax in [[y - 1, x - 1],
                               [y - 1, x],
                               [y - 1, x + 1],
                               [y, x - 1],
                               [y, x + 1],
                               [y + 1, x - 1],
                               [y + 1, x],
                               [y + 1, x + 1]]:
                    try:
                        if ay > -1 and ax > -1:
                            if data[ay][ax] == "#":
                                near += 1
                    except IndexError:
                        pass
                #If four or more are occupied, make it open
                if near >= 4:
                    newRow += "L"
                #Otherwise, leave it occupied
                else:
                    newRow += "#"
        #Add the row to the new list
        newSeats.append(newRow)
    #Return the new list
    return newSeats

def castingAdvance(data: list) -> list:
    """Advance the Game of Life state one iteration using raycasts."""

    #Create a new list to hold the advanced state
    newSeats: list = []
    #For each row...
    for y in range(len(data)):
        #Create a new string to hold the advanced row
        newRow: str = ""
        #For each character in the row...
        for x in range(len(data[0])):
            #If empty
            if data[y][x] == ".":
                #Add empty to row
                newRow += "."

            #If open
            elif data[y][x] == "L":
                #If the cast doesn't hit any occupied seats
                if cast((y, x), data) == 0:
                    #Make occupied
                    newRow += "#"
                else:
                    #Otherwise, leave open
                    newRow += "L"

            #If occupied
            elif data[y][x] == "#":
                #If the cast hits 5 or more
                if cast((y, x), data) >= 5:
                    #Make open
                    newRow += "L"
                else:
                    #Otherwise, leave occupied
                    newRow += "#"
        #Add the row to the new list
        newSeats.append(newRow)
    #Return the new list
    return newSeats

def cast(pos: tuple, data: list) -> int:

    hits: int = 0
    #For each direction...
    for _dir in [[-1, -1],
                 [-1, 0],
                 [-1, 1],
                 [0, -1],
                 [0, 1],
                 [1, -1],
                 [1, 0],
                 [1, 1]]:
        cy, cx = pos
        while True:
            #Advance once in the direction
            cy -= _dir[0]
            cx -= _dir[1]
            #If out of bounds, stop
            if cy < 0 or cx < 0 or cy >= len(data) or cx >= len(data[0]):
                break
            #If an open seat, stop
            if data[cy][cx] == "L":
                break
            #If an occupied seat, count and stop
            if data[cy][cx] == "#":
                hits += 1
                break
    #Return the count
    return hits

def part1(data: list) -> int:

    current: list = data
    _next: list = advance(data)
    #Run automation until it does not change
    while True:
        current = _next
        _next = advance(current)

        if current == _next:
            break

    count: int = 0
    #Count all of the occupied seats
    for y in current:
        for x in y:
            if x == "#":
                count += 1
    return count

def part2(data: list) -> int:

    current: list = data
    _next: list = castingAdvance(data)
    #Run automation until it does not change
    while True:
        current = _next
        _next = castingAdvance(current)

        if current == _next:
            break

    count: int = 0
    #Count all of the occupied seats
    for y in current:
        for x in y:
            if x == "#":
                count += 1
    return count

if __name__ == "__main__":

    #Load the input data
    data: list = load("seats.txt")
    #Print the answers for part 1 and 2
    print(f"Part 1: {part1(data)}\nPart 2: {part2(data)}")
