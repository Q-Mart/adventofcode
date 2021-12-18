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

def traverse_along_path(tree, path):
    if path == '':
        return tree

    if path[0] == 'l':
        return traverse_along_path(tree.left, path[1:])
    else:
        return traverse_along_path(tree.right, path[1:])

def rightmost(tree):
    if type(tree) == int:
        return tree
    else:
        return rightmost(tree.right)

def find_left_neighbour(tree, target, path):
    path_to_parent = path[:-1]
    parent = traverse_along_path(tree, path_to_parent)

    if parent.right == target:
        return rightmost(parent.left)
    else:
        return find_left_neighbour(tree, parent, path_to_parent)

def leftmost(tree):
    if type(tree) == int:
        return tree
    else:
        return rightmost(tree.left)

def find_right_neighbour(tree, target, path):
    path_to_parent = path[:-1]
    parent = traverse_along_path(tree, path_to_parent)

    if parent.left == target:
        return leftmost(parent.right)
    else:
        return find_right_neighbour(tree, parent, path_to_parent)


def parse_to_tree(data):
    if type(data) == int:
        return data
    else:
        return Node(parse_to_tree(data[0]), parse_to_tree(data[1]))

data = utils.get_day(2021, 18)

t = parse_to_tree([[6,[5,[4,[3,2]]]],1])
target, path = find_first_node_at_depth_4([(t, '')])
print(find_left_neighbour(t, target, path))
print(find_right_neighbour(t, target, path))
