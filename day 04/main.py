
def load(path: str) -> list:

    data: list = []
    with open(path) as f:
        return [line.strip() for line in f]

def convertToPassport(data: list) -> list:

    passports = []
    currentPassport = {}
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

    if validatePassport(passport) == False:
        return False

    if len(passport["byr"]) != 4 or int(passport["byr"]) < 1920 or int(passport["byr"]) > 2002:
        #print("Failed on \"byr\"")
        return False

    if len(passport["iyr"]) != 4 or int(passport["iyr"]) < 2010 or int(passport["iyr"]) > 2020:
        #print("Failed on \"iyr\"")
        return False

    if len(passport["eyr"]) != 4 or int(passport["eyr"]) < 2020 or int(passport["eyr"]) > 2030:
        #print("Failed on \"eyr\"")
        return False

    if passport["hgt"][-2:] != "cm" and passport["hgt"][-2:] != "in":
        #print("Failed on \"hgt\" cm/in")
        return False
    if passport["hgt"][-2:] == "cm" and not 150 <= int(passport["hgt"][:-2]) <= 193:
        #print("Failed on \"hgt\" cm size")
        return False
    if passport["hgt"][-2:] == "in" and not 59 <= int(passport["hgt"][:-2]) <= 76:
        #print("Failed on \"hgt\" in size")
        return False

    if len(passport["hcl"]) != 7 or passport["hcl"][0] != "#":
        #print("Failed on \"hcl\" #")
        return False
    for char in passport["hcl"][1:]:
        if char not in "0123456789abcdef":
            #print("Failed on \"hcl\" hex")
            return False

    if passport["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        #print("Failed on \"ecl\"")
        return False

    if len(passport["pid"]) != 9:
        #print("Failed on \"pid\" len")
        return False
    for char in passport["pid"]:
        if char not in "0123456789":
            #print("Failed on \"pid\" numeric")
            return False

    return True

def part1(passports: list) -> int:

    count: int = 0
    for passport in passports:
        if validatePassport(passport) == True:
            count += 1
    return count

def part2(passports: list) -> int:

    count: int = 0
    for passport in passports:
        if specificValidatePassport(passport) == True:
            count += 1
    return count

if __name__ == "__main__":

    data = load("passports.txt")
    passports = convertToPassport(data)
    
    print(f"Part 1: {part1(passports)}\nPart 2: {part2(passports)}")
