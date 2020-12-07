
def load(path: str) -> list:

    data: list = []
    with open(path) as f:
        return [line.strip() for line in f]

def part1(data: list) -> int:

    rules: dict = {}
    for line in data:
        words: list = line.split(" ")
        word: str = words[0] + " " + words[1]
        rule: list = []
        if "other" not in words:
            for i in range(4, len(words), 4):
                rule.append(words[i + 1] + " " + words[i + 2])
        rules[word] = rule

    while True:
        sanitized: bool = True
        for colorKey in rules.keys():
            for colorRule in rules[colorKey]:
                if colorRule != "shiny gold":
                    sanitized = False
                    rules[colorKey].remove(colorRule)
                    for colorAdd in rules[colorRule]:
                        rules[colorKey].append(colorAdd)

        if sanitized == True:
            break

    count: int = 0
    for colorKey in rules.keys():
        if "shiny gold" in rules[colorKey]:
            count += 1
    
    return count

def part2(data: list) -> int:

    rules: dict = {}
    for line in data:
        words: list = line.split(" ")
        word: str = words[0] + " " + words[1]
        rule: list = []
        if "other" not in words:
            for i in range(4, len(words), 4):
                for j in range(int(words[i])):
                    rule.append(words[i + 1] + " " + words[i + 2])
        rules[word] = rule

    count: int = -1

    bag = ["shiny gold"]
    while len(bag) > 0:
        color = bag.pop()
        count += 1
        for newBag in rules[color]:
            bag.append(newBag)

    return count

if __name__ == "__main__":

    data: list = load("colors.txt")
    print(f"Part 1: {part1(data)}\nPart 2: {part2(data)}")
