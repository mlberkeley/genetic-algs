
from random import random

import numpy as np

from data import Data
from evaluator import Evaluator
from mutations import Mutations
from tree_methods import TreeMethods

class Algorithm(object):
    @staticmethod
    def make_function(data, node_var):
        """ Generates a function.

            Args:
                data: Data object
                node_var: label for variable we are interested in

            Returns:
                sympy Function
        """
        TREE_COUNT = 10
        GENERATIONS = 50
        PROB_REPRODUCTION = 0.5
        PROB_POINT = 0.4
        PROB_CROSSOVER = 0.1

        # Generate a pool of trees
        #trees = [generate_tree() for _ in range(TREE_COUNT)]
        trees = [TreeMethods.create_full_tree(2) for _ in range(TREE_COUNT)]
        #for tree in trees:
        #    tree.ete_draw()

        for i in range(GENERATIONS):
            new_trees = []

            fitnesses = []
            for tree in trees:
                fitness = Evaluator.score(tree, data, node_var)
                fitnesses.append(fitness)
            fitnesses = np.array(fitnesses)

            # Translate and normalize fitnesses until they form a
            # probability distribution

            fitnesses += -np.min(fitnesses) + 1e-5
            fitnesses /= np.sum(fitnesses)

            while len(new_trees) <= TREE_COUNT:
                r = random()
                if r < PROB_POINT:
                    # Point mutation
                    candidate_tree = np.random.choice(trees, 1, p=fitnesses)[0]
                    tree = Mutations.mutate_point(candidate_tree)
                    new_trees.append(tree)
                elif r < PROB_POINT + PROB_CROSSOVER:
                    # Crossover mutation
                    [ctree1, ctree2] = np.random.choice(trees, 2, p=fitnesses)
                    tree1, tree2 = Mutations.mutate_crossover(ctree1, ctree2)
                    new_trees.append(tree1)
                    new_trees.append(tree2)
                else:
                    # Reproduction mutation
                    candidate_tree = np.random.choice(trees, 1, p=fitnesses)[0]
                    tree = candidate_tree.deepcopy()
                    new_trees.append(tree)

        # Return trees
        scores = [Evaluator.score(tree, data, node_var) for tree in trees]
        best_tree = trees[np.argmax(scores)]
        return best_tree.collapse()

if __name__ == "__main__":
    data = Data("pendulum.pkl")
    Algorithm.make_function(data, "x")
