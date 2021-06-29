#!/usr/local/bin/python3

def generate_rules():
    rules = {}
    with open('input.txt', 'r') as f:
        for line in f:
            outer, inner = parse_rule(line.rstrip())
            rules[outer] = inner
    return rules

def parse_rule(rule: str) -> (str, {}):
    outer = rule.split("contain")[0].replace(" bags ", "")
    inner = rule.split("contain")[1].rstrip()
    contains = {}
    if inner == " no other bags.":
        return outer, contains
    else:
        for contained in inner.split(","):
            contained = contained.strip().split(" ")
            amount = int(contained[0])
            color = contained[1] + " " + contained[2]
            contains[color] = amount
        return outer, contains

def contains(rules: {}, color: str) -> int:
    if rules[color] == {}:
        return 0
    total = 0
    for bag in rules[color]:
        weight = rules[color][bag]
        total = total + weight + weight*contains(rules, bag)
    return total

 
def main():
    rules = generate_rules() 
    color = 'shiny gold'
    total = contains(rules, color)
    
    print(total)
 
if __name__ == "__main__":
    main()

