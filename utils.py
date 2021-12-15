import queue
import heapq

def get_day(year, day_number):
    lines = []
    with open("{0}/inputs/{1}.txt".format(year, day_number)) as f:
        lines = f.readlines()
        lines = list(map(str.strip, lines))
    return lines

def bfs(start_state, goal_func, children_func):
    current_state = start_state
    visited = set(current_state)
    q = queue.Queue()
    while not goal_func(current_state):
        for child_state in children_func(current_state):
            if child_state in visited:
                continue
            else:
                q.put(child_state)

        if q.empty():
            return current_state

        current_state = q.get()

    return current_state

def dfs(start_state, goal_func, children_func):
    current_state = start_state
    visited = {current_state}
    stack = []
    while not goal_func(current_state):
        for child_state in children_func(current_state):
            if child_state in visited:
                continue
            else:
                stack.append(child_state)

        if len(stack) > 0:
            current_state = stack.pop()
        else:
            return current_state

    return current_state

def a_star(start, h_func, cost_func, moves_func):
    def get_path(previous, s):
        if s is None:
            return []

        path = []
        current = s
        while current in previous:
            path += [current]
            current = previous[current]

        path.reverse()
        return path

    frontier = [(h_func(start), start)]
    previous = {start: None}
    path_cost = {start: 0}

    while frontier:
        (f, s) = heapq.heappop(frontier)
        if h_func(s) == 0:
            return get_path(previous, s)

        for s2 in moves_func(s):
            new_cost = path_cost[s] + cost_func(s)
            if s2 not in path_cost or new_cost < path_cost[s2]:
                heapq.heappush(frontier, (new_cost + h_func(s2), s2))
                path_cost[s2] = new_cost
                previous[s2] = s

    return dict(fail=True, front=len(frontier), prev=len(previous))

def print_part_1(ans):
    print('{0}Part 1: {1}{2}'.format('\033[91m', ans, '\033[0m'))

def print_part_2(ans):
    print('{0}Part 2: {1}{2}'.format('\033[92m', ans, '\033[0m'))
