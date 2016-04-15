
from function import zero, one, add, sub
from random import shuffle

from ete3 import Tree as EteTree

class Node(object):
    def __init__(self, func):
        """ Node constructor.

            Args:
                func: Function object
        """
        self.func = func
        self.children = []

    def add_child(self, child):
        """ Adds a child to the node.

            Args:
                child: Node object

            Returns:
                None
        """
        self.children.append(child)

    def descendants_and_self(self):
        """ Returns all Node objects that are descendants of this Node
            as a set, including this node.

            Returns:
                set of Node objects
        """
        descendants = set()
        for child in self.children:
            descendants = descendants.union(child.descendants_and_self())
        descendants.add(self)
        return descendants

    def all_descendants_and_depths(self):
        """ Returns a set of tuples of all Node objects that are descendants of this
            Node and the depth of those nodes relative to this node.

            Returns:
                set of (Node, int) objects
        """
        # TODO
        descendants = set()
        for child in self.children:
            incremented_depths = [(node, depth + 1)
                                  for (node, depth)
                                  in child.all_descendants_and_depths()]
            descendants = descendants.union(incremented_depths)
        return descendants

    def grow(self, depth=None):
        """ Grows a random child node by 1, limited by `depth` (if provided)
            and arity restrictions.  Returns the new node (or None if no
            node can be expanded).

        Args:
            depth: int (default=None)

        Returns:
            Node instance (or None)
        """
        # TODO add depth constraint
        # Creates a random permutation of child nodes
        nodes = list(self.all_descendants())
        shuffle(nodes)

        for node in nodes:
            if len(node.children) >= node.func.arity:
                continue

            func = Function.random_function()
            node = Node(func)
            self.add_child(node)
            return node

        # If no children can be expanded, return None
        return None

    def __str__(self):
        if self.children:
            # TODO add self.label reference
            s = "({0});".format(",".join([str(child) for child in self.children]))
            return str(EteTree(s))
        else:
            return str(self.func)

if __name__ == "__main__":
    root = Node(add)
    a = Node(zero)
    b = Node(one)
    root.add_child(a)
    root.add_child(b)

    print(root)
    d = (root.descendants_and_self())
