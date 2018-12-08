import utils

memo = dict()

class Node:
    def __init__(self):
        self.children = []
        self.metadata = []

    def addChild(self, c):
        self.children.append(c)

    def addMetadata(self, m):
        self.metadata.append(m)

    def printTree(self, ID=0):
        print('{0}\t{1}'.format(ID, self.metadata))

        for c in self.children:
            ID += 1
            c.printTree(ID)

    def getMetadata(self):
        metadata = self.metadata[:]
        for c in self.children:
            metadata += c.getMetadata()

        return metadata

    def value(self):
        if self in memo:
            return memo[self]

        elif self.children == []:
            val = sum(self.metadata)
            memo[self] = val
            return val
        else:
            acc = 0
            for m in self.metadata:
                if 0 < m <= len(self.children):
                    acc += self.children[m-1].value()

            memo[self] = acc
            return acc


def createNode(i, data):
    node = Node()

    numChildren = data[i]
    numMetadata = data[i+1]

    i += 2

    for c in range(numChildren):
        n, i = createNode(i, data)
        node.addChild(n)

    for m in range(numMetadata):
        node.addMetadata(data[i+m])

    return node, i+numMetadata

data = list(map(int, utils.getDay(8)[0].split()))
# data = list(map(int, '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'.split()))

root, _ = createNode(0, data)
print (sum(root.getMetadata()))
print (root.value())
