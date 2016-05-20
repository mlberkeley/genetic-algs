
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
    
    @staticmethod
    def mutate_float(node, score_tree, eps=1e-1):
        """ Takes a Node object and optimizes floats greedily.
            Returns a new tree.

            Args:
                node: Node object to operate on
                score_tree: function that takes a tree
                    and returns a fitness (as float)
                eps: learning rate (as float) (default=1e-1)

            Returns:
                Node object
        """
        # Copy the tree
        new_tree = node.deepcopy()

        # Find all floating leaves
        floats = new_tree.all_floats()
        if floats == []:
            return None

        has_changed = False

        for f in floats:
            value = f.func.func()
            left_value = value - eps
            right_value = value + eps

            func = f.func
            left_func = Function.make_float_function(left_value)
            left_func = Function(left_func, 0, str(left_value))
            right_func = Function.make_float_function(right_value)
            right_func = Function(right_func, 0, str(right_value))

            score = score_tree(new_tree)
            f.func = left_func
            left_score = score_tree(new_tree)
            f.func = right_func
            right_score = score_tree(new_tree)

            max_ = max(left_score, score, right_score)
            if abs(max_ - left_score) < 1e-10:
                f.func = left_func
                has_changed = True
            elif abs(max_ - right_score) < 1e-10:
                f.func = right_func
                has_changed = True
            else:
                f.func = func

        if not has_changed:
            return None

        return new_tree
