import utils
from collections import defaultdict, namedtuple

State = namedtuple('State', ['current_path', 'visited_paths', 'graph'])

def to_graph(data):
    graph = defaultdict(set)
    for line in data:
        a, b = line.split('-')
        graph[a].add(b)
        graph[b].add(a)

    return graph

def goal_func(state):
    path = state.current_path
    return 'start' in path and 'end' in path

def children_func(state):
    children = []

    current_node = state.current_path[-1]
    new_nodes = state.graph[current_node]
    for node in new_nodes:
        if node.islower() and state.current_path.count(node) > 1:
            continue

        new_path = state.current_path+[node]
        if new_path in state.visited_paths:
            continue

        children.append(
            State(
                current_path=state.current_path+[node],
                visited_paths=state.visited_paths,
                graph=state.graph
            )
        )

def search(graph, path=['start']):
    if 'start' in path and 'end' in path:
        return [path]

    visited = []

    current_node = path[-1]
    for new_node in graph[current_node]:
        if new_node.islower() and path.count(new_node) >= 1:
            continue

        new_path = path + [new_node]
        new_paths = search(graph, new_path)
        visited += new_paths

    return visited

def search2(graph, revisit_node, visited_paths, path=['start']):
    if 'start' in path and 'end' in path:
        if path not in visited_paths:
            return [path]
        else:
            return []

    visited = []

    current_node = path[-1]
    for new_node in graph[current_node]:
        if new_node.islower():

            if new_node == revisit_node:
                if path.count(new_node) >= 2:
                    continue

            if path.count(new_node) >= 1:
                    continue

        new_path = path + [new_node]
        new_paths = search2(graph, revisit_node, visited_paths, new_path)
        visited += new_paths

    return visited

def search_and_visit_small_cave_at_most_twice(graph):
    small_caves = set()
    for to, fro in graph.items():
        if to.islower():
            small_caves.add(to)

        small_caves.update([f for f in fro if f.islower()])

    # Remove start and end
    small_caves -= {'start', 'end'}

    visited = []
    for cave in small_caves:
        # print(cave)
        visited += search2(graph, cave, visited)
        # print(visited)

    return visited

test_data_1 = [
    'start-A',
    'start-b',
    'A-c',
    'A-b',
    'b-d',
    'A-end',
    'b-end'
]

test_data_2 = [
    'dc-end',
    'HN-start',
    'start-kj',
    'dc-start',
    'dc-HN',
    'LN-dc',
    'HN-end',
    'kj-sa',
    'kj-HN',
    'kj-dc'
]

test_data_3 = [
    'fs-end',
    'he-DX',
    'fs-he',
    'start-DX',
    'pj-DX',
    'end-zg',
    'zg-sl',
    'zg-pj',
    'pj-he',
    'RW-he',
    'fs-DX',
    'pj-RW',
    'zg-RW',
    'start-pj',
    'he-WI',
    'zg-he',
    'pj-fs',
    'start-RW'
]

data = utils.get_day(2021, 12)

assert len(search(to_graph(test_data_1))) == 10
assert len(search(to_graph(test_data_2))) == 19
assert len(search(to_graph(test_data_3))) == 226

utils.print_part_1(len(search(to_graph((data)))))

result = search_and_visit_small_cave_at_most_twice((to_graph(test_data_1)))
print(len(result))
