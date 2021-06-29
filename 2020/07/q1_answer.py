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

def contained_by(rules: {}, colors: [], depth=[]) -> []:
    if not colors:
        return depth
    layer = []
    for rule in rules:
        for color in colors:
            if color in rules[rule].keys():
                if rule not in layer:
                    layer = layer + [rule]
    depth.append(layer)
    contained_by(rules, layer, depth)
        
def main():
    rules = generate_rules() 
    color = ['shiny gold']
    tree = []
    contained_by(rules, color, tree)
    final = []
    for layer in tree:
        for color in layer:
            if color not in final:
                final = final + [color]
    print(len(final))
 
if __name__ == "__main__":
    main()

