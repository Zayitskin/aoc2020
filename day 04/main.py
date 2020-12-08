
def load(path: str) -> list:
    """Load the input from a file."""
    data: list = []
    with open(path) as f:
        return [line.strip() for line in f]

def convertToPassport(data: list) -> list:
    """Convert the input into a list of passport dicts."""
    passports: list = []
    currentPassport: dict = {}
    for line in data:
        if line == "":
            passports.append(currentPassport)
            currentPassport = {}
        else:
            for bit in line.split(" "):
                key, value = bit.split(":")
                currentPassport[key] = value

    passports.append(currentPassport)

    return passports

def validatePassport(passport: dict) -> bool:
    """Return if a passport is valid."""
    #A passport is valid if all of the following manditory parameters exist
    if "byr" not in passport:
        return False
    if "iyr" not in passport:
        return False
    if "eyr" not in passport:
        return False
    if "hgt" not in passport:
        return False
    if "hcl" not in passport:
        return False
    if "ecl" not in passport:
        return False
    if "pid" not in passport:
        return False
    return True

def specificValidatePassport(passport: dict) -> bool:
    """Return if a passport is valid to the more specific contraints."""
    #Passport must still pass the original constraints
    if validatePassport(passport) == False:
        return False

    #1920 <= byr <= 2002
    if len(passport["byr"]) != 4 or int(passport["byr"]) < 1920 or int(passport["byr"]) > 2002:
        return False

    #2010 <= iyr <= 2020
    if len(passport["iyr"]) != 4 or int(passport["iyr"]) < 2010 or int(passport["iyr"]) > 2020:
        return False

    #2020 <= eyr <= 2030
    if len(passport["eyr"]) != 4 or int(passport["eyr"]) < 2020 or int(passport["eyr"]) > 2030:
        return False

    #hgt ends in either cm or in with specific integer constraints for each
    if passport["hgt"][-2:] != "cm" and passport["hgt"][-2:] != "in":
        return False
    if passport["hgt"][-2:] == "cm" and not 150 <= int(passport["hgt"][:-2]) <= 193:
        return False
    if passport["hgt"][-2:] == "in" and not 59 <= int(passport["hgt"][:-2]) <= 76:
        return False

    #hcl starts with # and only contains hex characters
    if len(passport["hcl"]) != 7 or passport["hcl"][0] != "#":
        return False
    for char in passport["hcl"][1:]:
        if char not in "0123456789abcdef":
            return False

    #ecl must be in the list
    if passport["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False

    #pid must be nine numbers
    if len(passport["pid"]) != 9:
        return False
    for char in passport["pid"]:
        if char not in "0123456789":
            return False

    return True

def part1(passports: list) -> int:

    #Count all passports that pass the simple validation
    count: int = 0
    for passport in passports:
        if validatePassport(passport) == True:
            count += 1
    return count

def part2(passports: list) -> int:

    #Count all passports that pass the specific validation
    count: int = 0
    for passport in passports:
        if specificValidatePassport(passport) == True:
            count += 1
    return count

if __name__ == "__main__":

    #Load the input data and convert to passports
    data: list = load("passports.txt")
    passports: list = convertToPassport(data)
    #Print the answers for part 1 and 2
    print(f"Part 1: {part1(passports)}\nPart 2: {part2(passports)}")
