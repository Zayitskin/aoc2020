
def load(path: str) -> list:
    """Load the input from a file."""
    data: list = []
    with open(path) as f:
        return [line.strip() for line in f]

def rotate(wayx: int, wayy: int, angle: int) -> [int, int]:
    """Rotate an XY coordinate pair some multiple of 90 degrees."""
    
    if angle % 360 == 0:
        return wayx, wayy
    elif angle % 360 == 90:
        return wayy, -wayx
    elif angle % 360 == 180:
        return -wayx, -wayy
    elif angle % 360 == 270:
        return -wayy, wayx

def part1(data: list) -> int:

    facing: int = 0
    posx: int = 0
    posy: int = 0

    #For each order...
    for order in data:
        #N: Go up
        if order[0] == "N":
            posy += int(order[1:])
        #S: Go down
        elif order[0] == "S":
            posy -= int(order[1:])
        #E: Go right
        elif order[0] == "E":
            posx += int(order[1:])
        #W: Go left
        elif order[0] == "W":
            posx -= int(order[1:])
        #L: Rotate facing to the left
        elif order[0] == "L":
            facing -= int(order[1:])
        #R: Rotate facing to the reft
        elif order[0] == "R":
            facing += int(order[1:])
        #Go in the direction of the current facing
        elif order[0] == "F":
            if facing % 360 == 0:
                posx += int(order[1:])
            elif facing % 360 == 90:
                posy -= int(order[1:])
            elif facing % 360 == 180:
                posx -= int(order[1:])
            elif facing % 360 == 270:
                posy += int(order[1:])

    #Return the Manhatten distance from the start
    return abs(posx) + abs(posy)

def part2(data: list) -> int:

    wayx: int = 10
    wayy: int = 1
    posx: int = 0
    posy: int = 0

    for order in data:
        #Move the waypoint up
        if order[0] == "N":
            wayy += int(order[1:])
        #Move the waypoint down
        elif order[0] == "S":
            wayy -= int(order[1:])
        #Move the waypoint right
        elif order[0] == "E":
            wayx += int(order[1:])
        #Move the waypoint left
        elif order[0] == "W":
            wayx -= int(order[1:])
        #Rotate the waypoint around the boat to the left
        elif order[0] == "L":
            wayx, wayy = rotate(wayx, wayy, int(order[1:]) * -1)
        #Rotate the waypoint around the boat to the right
        elif order[0] == "R":
            wayx, wayy = rotate(wayx, wayy, int(order[1:]))
        #Move the boat according to the waypoint
        elif order[0] == "F":
            posx += wayx * int(order[1:])
            posy += wayy * int(order[1:])

    #Return the Manhatten distance from the start
    return abs(posx) + abs(posy)

if __name__ == "__main__":

    #Load the input data
    data: list = load("orders.txt")
    #Print the answers for part 1 and 2
    print(f"Part 1: {part1(data)}\nPart 2: {part2(data)}")
