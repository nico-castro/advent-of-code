#!/usr/local/bin/python3
import ipdb

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

def validate_passport(passport: dict) -> bool:
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for field in required_fields:
        if passport.get(field) == '':
            return False
    return True

valid = 0
for passport in passports:
    if validate_passport(passport):
       valid = valid + 1

print(valid)
