
import sympy as sy
from function import add, Function
from random import shuffle, choice

from config import Cfg
if Cfg.USE_ETE3:
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

    def all_floats(self):
        """ Returns all float leaves.  If there are
            no leaves, return [].

            Returns:
                list of Node objects
        """
        all_floats = [d
                      for d
                      in self.descendants_and_self()
                      if d.func.arity == 0 and
                      isinstance(d.func.func(), sy.Float)]
        return all_floats

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
            nodes = [node for node in self.descendants_and_self()
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

            if d == depth - 1:
                func = Function.random_terminal()
            else:
                func = Function.random_function()
            child = Node(func)
            node.add_child(child)
            return child

        # If no children can be expanded, return None
        return None

    def ete_str_nosemi(self):
        # TODO document
        if Cfg.USE_ETE3:
            if self.children:
                s = ",".join([c.ete_str_nosemi() for c in self.children])
                return "({0}){1}".format(s, self.func.label)
            else:
                return self.func.label
        else:
            return ""

    def ete_str(self):
        # TODO document
        if Cfg.USE_ETE3:
            return "{0};".format(self.ete_str_nosemi())
        else:
            return ""

    def ete_print(self):
        """ Pretty print.
        
            TODO Debug and document better for case USE_ETE3 == False
        """
        if Cfg.USE_ETE3:
            t = EteTree(self.ete_str(), format=1)
            print(t.get_ascii(show_internal=True))
        else:
            return str(self)

    def ete_draw(self, fname=None):
        """ Draws the tree and saves it to a file.  If `fname` is None,
            show the tree instead of saving it.

            Args:
                fname: filename to save to (default=None)
        """
        if Cfg.USE_ETE3:
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
        else:
            # TODO maybe throw an error?
            pass

    def collapse(self):
        """ Returns the sympy function corresponding to this node.

            Returns:
                sympy Function
        """
        # TODO this is wrong!!!!!!!
        # TODO is it wrong??
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
    pass
