
""" Tree class. """

from ete3 import Tree as EteTree

class Tree:
    def __init__(self, node, children=None):
        self.node = node
        self.children = children 
        
    def get_children(self):
        return children

    def entry(self):
        return self.node

    def isLeaf(self):
        return bool(self.children)

    def add_child(self, child):
        if self.children:
            self.children.append(child)
        else:
            self.children = [child]

    def __str__(self):
        if self.children:
            s = "({0});".format(",".join([str(child) for child in self.children]))
            return str(EteTree(s))
        else:
            return str(self.node.value.num)
