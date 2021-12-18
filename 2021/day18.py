import utils
import math

class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Node(l={self.left}, r={self.right})'

def split(num):
    return Node(math.floor(num/2), math.ceil(num/2))

def find_first_node_at_depth_4(stack):
    print(stack)
    if stack == []:
        return None

    node, path = stack.pop()
    if len(path) >= 4:
        return node, path

    if type(node.left) == Node:
        stack.append((node.left, path+'l'))

    if type(node.right) == Node:
        stack.append((node.right, path+'r'))

    return find_first_node_at_depth_4(stack)

def find_left_neighbour(tree, path):
    path = path[:-1]

def parse_to_tree(data):
    if type(data) == int:
        return data
    else:
        return Node(parse_to_tree(data[0]), parse_to_tree(data[1]))

data = utils.get_day(2021, 18)

t = parse_to_tree([[6,[5,[4,[3,2]]]],1])
print(find_first_node_at_depth_4([(t, '')]))
