import utils

class Node:
    def __init__(self, left, right):
        self.left = left,
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

def parse_to_tree(data):
    print(data)
    if type(data) == int:
        return data
    else:
        return Node(parse_to_tree(data[0]), parse_to_tree(data[1]))

data = utils.get_day(2021, 18)

print(parse_to_tree([[[[[9,8],1],2],3],4]))
