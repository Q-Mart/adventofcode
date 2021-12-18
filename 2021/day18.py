import utils
import math

class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Node(l={self.left}, r={self.right})'

def equal_trees(t1, t2):
    if type(t1) == type(t2):
        if type(t1) == int:
            return t1 == t2
        else:
            return equal_trees(t1.left, t2.left) and equal_trees(t1.right, t2.right)

    return False

def split(num):
    return Node(math.floor(num/2), math.ceil(num/2))

def find_first_node_at_depth_4(stack):
    if stack == []:
        return None

    node, path = stack.pop()
    if len(path) >= 4:
        return node, path

    if type(node.right) == Node:
        stack.append((node.right, path+'r'))

    if type(node.left) == Node:
        stack.append(((node.left, path+'l')))

    return find_first_node_at_depth_4(stack)

def traverse_along_path(tree, path):
    if path == '':
        return tree

    if path[0] == 'l':
        return traverse_along_path(tree.left, path[1:])
    else:
        return traverse_along_path(tree.right, path[1:])

def rightmost(tree, path=''):
    if type(tree) == int:
        return tree, path
    else:
        return rightmost(tree.right, path+'r')

def find_left_neighbour(tree, target, path):
    if path == '':
        return None

    path_to_parent = path[:-1]
    parent = traverse_along_path(tree, path_to_parent)

    if parent.right == target:
        return rightmost(parent.left, path_to_parent+'l')
    else:
        return find_left_neighbour(tree, parent, path_to_parent)

def leftmost(tree, path=''):
    if type(tree) == int:
        return tree, path
    else:
        return leftmost(tree.left, path+'l')

def find_right_neighbour(tree, target, path):
    if path == '':
        return None

    path_to_parent = path[:-1]
    parent = traverse_along_path(tree, path_to_parent)

    if parent.left == target:
        return leftmost(parent.right, path_to_parent+'r')
    else:
        return find_right_neighbour(tree, parent, path_to_parent)

def explode(tree, target, path_to_target):
    _, leftmost_path = leftmost(tree)
    if traverse_along_path(tree, leftmost_path[:-1]) == target:
        parent = traverse_along_path(tree, leftmost_path[:-2])
        parent.left = 0
        parent.right = parent.right + target.right
        return tree

    _, rightmost_path = leftmost(tree)
    if traverse_along_path(tree, rightmost_path[:-1]) == target:
        parent = traverse_along_path(tree, rightmost_path[:-2])
        parent.right = 0
        parent.left = parent.left + target.left
        return tree

    r = find_left_neighbour(tree, target, path_to_target)
    if r != None:
        _, left_neighbour_path = r
        final_step_to_left_neighbour = left_neighbour_path[-1]
        left_neighbour_parent = traverse_along_path(tree, left_neighbour_path[:-1])

        if final_step_to_left_neighbour == 'r':
            left_neighbour_parent.right += target.left
        else:
            left_neighbour_parent.left += target.left

    r = find_right_neighbour(tree, target, path_to_target)
    if r != None:
        r, right_neighbour_path = r
        final_step_to_right_neighbour = right_neighbour_path[-1]
        right_neighbour_parent = traverse_along_path(tree, right_neighbour_path[:-1])

        if final_step_to_right_neighbour == 'r':
            right_neighbour_parent.right += target.right
        else:
            right_neighbour_parent.left += target.right

    parent = traverse_along_path(tree, path_to_target[:-1])
    if parent.left == target:
        parent.left = 0
    else:
        parent.right = 0

    return tree

def parse_to_tree(data):
    if type(data) == int:
        return data
    else:
        return Node(parse_to_tree(data[0]), parse_to_tree(data[1]))

def assert_explode(data, expected_data):
    t = parse_to_tree(data)
    expected_t = parse_to_tree(expected_data)

    target, path = find_first_node_at_depth_4([(t, '')])

    t = explode(t, target, path)
    assert equal_trees(t, expected_t)

data = utils.get_day(2021, 18)

assert_explode([[[[[9,8],1],2],3],4], [[[[0,9],2],3],4])
assert_explode([7,[6,[5,[4,[3,2]]]]], [7,[6,[5,[7,0]]]])
assert_explode([[6,[5,[4,[3,2]]]],1], [[6,[5,[7,0]]],3])
assert_explode([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]], [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]])
assert_explode([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]], [[3,[2,[8,0]]],[9,[5,[7,0]]]])
