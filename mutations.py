
from random import choice, randint
from function import Function
from tree_methods import TreeMethods

class Mutations(object):
    @staticmethod
    def mutate_point(node):
        """ Takes a Node object and randomly mutates one of its descendants
            (or itself) \strikeout{into a function with the same arity. Preserves the
            original tree.} generates a new tree off a random child.

            Returns:
                Node object
        """

        if len(node.children) == 0:
            return TreeMethods.create_grow_tree(5)
        else:
            # Copy the tree
            new_tree = node.deepcopy()

            # Pick a descendant
            descendant = new_tree.random_descendant(with_leaves=False)

            # Pick a child

            # Make a new tree
            child = TreeMethods.create_grow_tree(5)
            p = randint(0, len(descendant.children) - 1)
            descendant.children[p] = child

            ## Pick a function with the same parity
            #arity = descendant.func.arity
            #func = Function.random_function(arity)

            ## Mutate new tree
            #descendant.func = func

            return new_tree

    @staticmethod
    def mutate_crossover(node1, node2):
        """ Takes two Node objects and finds two descendants of same arity
            and replaces one branch with the other.  Preserves the original
            trees.

            Returns:
                (Node, Node) tuple
        """
        # TODO change probability based on depth

        # Copy trees
        new_tree1 = node1.deepcopy()
        new_tree2 = node2.deepcopy()

        # Find two nonleaf descendants
        descendant1 = new_tree1.random_descendant(with_leaves=False)
        descendant2 = new_tree2.random_descendant(with_leaves=False)

        # Find two random children of those descendants
        child_index1 = randint(0, len(descendant1.children) - 1)
        child_index2 = randint(0, len(descendant2.children) - 1)

        # Cross over children
        descendant1.children[child_index1], descendant2.children[child_index2] = \
            descendant2.children[child_index2], descendant1.children[child_index1]

        return (new_tree1, new_tree2)
