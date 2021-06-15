#!/usr/local/bin/python3
import re


def val_byr(byr: int) -> bool:
    if byr < 1920 or byr > 2002:
        return False
    else:
        return True

def val_iyr(iyr: int) -> bool:
    if iyr < 2010 or iyr > 2020:
        return False
    else:
        return True

def val_eyr(eyr: int) -> bool:
    if eyr < 2020 or eyr > 2030:
        return False
    else:
        return True

def val_hgt(hgt: str) -> bool:
    if hgt[-2:] == 'cm':
        hgt = int(hgt.rstrip('cm'))
        if hgt >= 150 and hgt <= 193:
            return True
    elif hgt[-2:] == 'in':
        hgt = int(hgt.rstrip('in'))
        if hgt >= 59 and hgt <= 76:
            return True
    return False

def val_hcl(hcl: str) -> bool:
    try:
        valid = re.fullmatch("^#[0-9a-f]{6}", hcl).group(0)
    except AttributeError:
        return False
    return True

def val_ecl(ecl: str) -> bool:
    return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def val_pid(pid: str) -> bool:
    try:
        valid = re.fullmatch("\d{9}", pid).group(0)
    except AttributeError:
        return False
    return True

def validate_passport(passport: dict) -> bool:
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for field in required_fields:
        if passport.get(field) == '':
            return False
    return val_byr(int(passport['byr'])) and \
           val_iyr(int(passport['iyr'])) and \
           val_eyr(int(passport['eyr'])) and \
           val_hgt(passport['hgt']) and \
           val_hcl(passport['hcl']) and \
           val_ecl(passport['ecl']) and \
           val_pid(passport['pid'])



def main():
    passports = []
    with open('input.txt', 'r') as file:
        passport = {'byr': '', 'iyr': '', 'eyr': '', 'hgt': '', 'hcl': '', 'ecl': '', 'pid': '',  'cid': ''}       
        for line in file:
            if line == '\n':
                # start fresh passport
                passports.append(passport)
                passport = {'byr': '', 'iyr': '', 'eyr': '', 'hgt': '', 'hcl': '', 'ecl': '', 'pid': '',  'cid': ''}       
            pairs = line.split(' ')
            for pair in pairs:
                if pair == '\n':
                    continue
                passport[str(pair.split(':')[0])] = pair.split(':')[1].rsplit()[0]
        passports.append(passport)
    
    valid = 0
    for passport in passports:
        if validate_passport(passport):
           valid = valid + 1
    
    print(valid)

if __name__ == "__main__":
    main()
