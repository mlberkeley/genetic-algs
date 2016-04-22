
from function import zero, one, add
from random import shuffle, choice

from ete3 import Tree as EteTree, TreeStyle, NodeStyle, faces, AttrFace

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

    def descendants_and_self_with_depths(self):
        """ Returns a set of tuples of all Node objects that are descendants of this
            Node and the depth of those nodes relative to this node.

            Returns:
                set of (Node, int) objects
        """
        descendants = set()
        for child in self.children:
            incremented_depths = [(node, depth + 1)
                                  for (node, depth)
                                  in child.descendants_and_self_with_depths()]
            descendants = descendants.union(incremented_depths)
        descendants.add((self, 0))
        return descendants

    def only_descendants(self):
        """ Returns all Node objects that are descendants of this Node
            as a set, not including this node.

            Returns:
                set of Node objects
        """
        descendants = set()
        for child in self.children:
            descendants = descendants.union(child.descendants_and_self())
        return descendants

    def random_descendant(self, with_leaves=False):
        """ Returns a random descendant (not including itself).

            Args:
                with_leaves: boolean for whether to include leaves

            Returns:
                Node object
        """
        if with_leaves:
            return choice(self.only_descendants())
        else:
            nodes = [node for node in self.only_descendants()
                          if len(node.children) > 0]
            if len(nodes) == 0:
                # ERROR
                # fuck it
                # TODO throw real error messages
                1 / 0
            return choice(nodes)

    def random_child(self):
        """ Returns a random child.

            Returns:
                Node object
        """
        return choice(self.children)

    def grow(self, depth=None):
        """ Grows a random child node by 1, limited by `depth` (if provided)
            and arity restrictions.  Returns the new node (or None if no
            node can be expanded).

        Args:
            depth: int (default=None)

        Returns:
            Node instance (or None)
        """
        # Creates a random permutation of child nodes
        nodes_depths = list(self.descendants_and_self_with_depths())
        shuffle(nodes_depths)

        for node, d in nodes_depths:
            if len(node.children) >= node.func.arity:
                continue

            if d >= depth:
                continue

            func = Function.random_function()
            node = Node(func)
            self.add_child(node)
            return node

        # If no children can be expanded, return None
        return None

    def ete_str_nosemi(self):
        if self.children:
            s = ",".join([c.ete_str_nosemi() for c in self.children])
            return "({0}){1}".format(s, self.func.label)
        else:
            return self.func.label

    def ete_str(self):
        return "{0};".format(self.ete_str_nosemi())

    def ete_print(self):
        """ Pretty print. """
        t = EteTree(self.ete_str(), format=1)
        print(t.get_ascii(show_internal=True))

    def ete_draw(self, fname=None):
        """ Draws the tree and saves it to a file.  If `fname` is None,
            show the tree instead of saving it.

            Args:
                fname: filename to save to (default=None)
        """
        def layout(node):
            faces.add_face_to_node(AttrFace("name"), node, column=0,
                                   position="branch-right")

        ts = TreeStyle()
        ts.show_leaf_name = False
        ts.layout_fn = layout
        ts.rotation = 90
        
        tree = EteTree(self.ete_str(), format=8)

        if fname:
            tree.render(fname, tree_style=ts)
        else:
            tree.show(tree_style=ts)

    def collapse(self):
        """ Returns the sympy function corresponding to this node.

            Returns:
                sympy Function
        """
        # TODO this is wrong!!!!!!!
        if self.func.arity == 0:
            return self.func.evaluate()
        else:
            args = [child.collapse() for child in self.children]
            return self.func.evaluate(*args)

    def deepcopy(self):
        """ Return a deep copy of this Node and its descendants.

            Returns:
                Node object
        """
        new_root = Node(self.func)
        new_root.children = [child.deepcopy() for child in self.children]

        return new_root

if __name__ == "__main__":
    root = Node(add)
    a = Node(zero)
    b = Node(one)
    root.add_child(a)
    root.add_child(b)

    print(root)
    d = root.descendants_and_self_with_depths()
    print(d)
    d = root.descendants_and_self()
    print(d)
