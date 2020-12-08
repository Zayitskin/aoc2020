
def load(path: str) -> list:
    """Load the input from a file."""
    data: list = []
    with open(path) as f:
        return [line.strip() for line in f]

def part1(data: list) -> int:

    #Dictionary for color rules
    rules: dict = {}
    for line in data:
        #Unpack each rule line into its component parts
        words: list = line.split(" ")
        word: str = words[0] + " " + words[1]
        rule: list = []
        #Add each compontent to the rule
        if "other" not in words:
            for i in range(4, len(words), 4):
                rule.append(words[i + 1] + " " + words[i + 2])
        rules[word] = rule

    #Simplify all of the rules
    while True:
        sanitized: bool = True
        for colorKey in rules.keys():
            for colorRule in rules[colorKey]:
                #If there is a color and it is not shiny gold, then it
                #still can be simplified further
                if colorRule != "shiny gold":
                    sanitized = False
                    rules[colorKey].remove(colorRule)
                    for colorAdd in rules[colorRule]:
                        rules[colorKey].append(colorAdd)

        if sanitized == True:
            break

    #Count up all the rules that have at least one shiny gold in them
    count: int = 0
    for colorKey in rules.keys():
        if "shiny gold" in rules[colorKey]:
            count += 1
    
    return count

def part2(data: list) -> int:

    #Dictionary for color rules
    rules: dict = {}
    for line in data:
        #Unpack each rule line into its component parts
        words: list = line.split(" ")
        word: str = words[0] + " " + words[1]
        rule: list = []
        #Add each compontent to the rule equal to the number associated with it
        if "other" not in words:
            for i in range(4, len(words), 4):
                for j in range(int(words[i])):
                    rule.append(words[i + 1] + " " + words[i + 2])
        rules[word] = rule

    #Start the count at -1 as to only count the contents inside the bag
    count: int = -1
    #Populate the container with the base case
    bag: list[str] = ["shiny gold"]
    
    #Keep running until all bags have been handled
    while len(bag) > 0:
        #Take a bag out of the container and count it
        color: str = bag.pop()
        count += 1
        #Populate the container with all the bags that must be inside the
        #removed bag according to the rules
        for newBag in rules[color]:
            bag.append(newBag)

    return count

if __name__ == "__main__":

    #Load the input data
    data: list = load("colors.txt")
    #Print the answers for part 1 and 2
    print(f"Part 1: {part1(data)}\nPart 2: {part2(data)}")
