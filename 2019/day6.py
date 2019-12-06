import utils
from collections import defaultdict

data = utils.get_day(2019, 6)

def generate_graph(data):
    orbits = defaultdict(set)
    for string in data:
        planet_1, planet_2 = string.split(')')
        orbits[planet_1] |= {planet_2}

    return orbits

def number_of_direct_orbits(graph):
    result = 0
    for planet, v in list(graph.items()):
        result += len(graph[planet])

    return result

def get_indirect_orbits(planet, direct_orbits, indirect_orbits):
    node = planet
    stack = list()
    while node != None:
        kids = direct_orbits[node]
        stack += list(kids)
        indirect_orbits[planet] |= kids

        node = stack.pop() if stack else None

def number_of_indirect_orbits(graph):
    result = 0
    indirect_orbits = defaultdict(set)

    for planet, _ in list(graph.items()):
        get_indirect_orbits(planet, graph, indirect_orbits)

    for _, v in indirect_orbits.items():
        result += len(v)

    return result


def checksum(graph):
    return number_of_indirect_orbits(graph)

test = ['COM)B',
        'B)C',
        'C)D',
        'D)E',
        'E)F',
        'B)G',
        'G)H',
        'D)I',
        'E)J',
        'J)K',
        'K)L',]
assert(checksum(generate_graph(test)) == 42)
utils.print_part_1(checksum(generate_graph(data)))
