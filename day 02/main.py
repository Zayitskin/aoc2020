from collections import Counter

def load(path: str) -> list[dict]:
    """Load the input from a file."""
    data: list = []

    with open(path) as f:
        for line in f:
            _range, char, password = line.split()
            lower, upper = _range.split("-")
            data.append({
                "lower": int(lower),
                "upper": int(upper),
                "char": char[0],
                "password": password,
                })
    return data

def validatePassword1(lower: int, upper: int, char: str, password: str) -> bool:
    """Password validation for part 1."""
    counter: Counter = Counter(password)
    if counter[char] < lower or counter[char] > upper:
        return False
    else:
        return True

def validatePassword2(lower: int, upper: int, char: str, password: str) -> bool:
    """Password validation for part 2."""
    if password[lower - 1] == char and password[upper - 1] != char:
        return True
    elif password[lower - 1] != char and password[upper - 1] == char:
        return True
    else:
        return False

def part1(data: list[dict]) -> int:

    count: int = 0
    for d in data:
        if validatePassword1(d["lower"], d["upper"], d["char"], d["password"]):
            count += 1
    return count

def part2(data: list[dict]) -> int:

    count: int = 0
    for d in data:
        if validatePassword2(d["lower"], d["upper"], d["char"], d["password"]):
            count += 1
    return count

if __name__ == "__main__":

    #Load the input data
    data: list = load("passwords.txt")
    #Print the answers for part 1 and 2
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
