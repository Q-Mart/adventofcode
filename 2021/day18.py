import utils
import math

class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    # def explode_left(self, val=None):
    #     if val == None:
    #         val = self.left

    #     if self.parent == None:
    #         return False
    #     elif self.parent.left != self:
    #         self.parent.left += val
    #         return True
    #     else:
    #         return self.parent.explode_left(val)

    def __repr__(self):
        return f'Node(l={self.left}, r={self.right})'

def split(num):
    return Node(math.floor(num/2), math.ceil(num/2))

def traverse(tree, path=''):
    if len(path) >= 4:
        return tree, path

    if type(tree.left) == list:
        result = traverse(tree.left, path+'l')
        if result != None:
            return result

    if type(tree.right) == list:
        result = traverse(tree.right, path+'r')
        if result != None:
            return result

    return None

def find_first_node_at_depth(tree, depth=4, current_depth=0):
    if current_depth == depth:
        return tree
    elif type(tree) == int:
        # Can't go lower
        return None
    else:
        return find_first_node_at_depth(tree.left, depth, current_depth+1)

def parse_to_tree(data):
    if type(data) == int:
        return data
    else:
        return Node(parse_to_tree(data[0]), parse_to_tree(data[1]))

data = utils.get_day(2021, 18)

t = parse_to_tree([[6,[5,[4,[3,2]]]],1])
print(traverse(t))
