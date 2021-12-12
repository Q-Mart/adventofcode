import utils
from collections import defaultdict, namedtuple

State = namedtuple('State', ['current_path', 'visited_paths', 'graph'])

def to_graph(data):
    graph = defaultdict(list)
    for line in data:
        a, b = line.split('-')
        graph[a].append(b)

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


test_data_1 = [
    'start-A',
    'start-b',
    'A-c',
    'A-b',
    'b-d',
    'A-end',
    'b-end'
]

test_start_1 = State(current_path=['start'], visited_paths=[], graph=to_graph(test_data_1))
print(utils.bfs(test_start_1, goal_func, children_func))

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
