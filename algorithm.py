
import numpy as np

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
        TREE_COUNT = 100
        GENERATIONS = 50
        PROB_REPRODUCTION = 0.5
        PROB_POINT = 0.4
        PROB_CROSSOVER = 0.1

        # Generate a pool of trees
        trees = [generate_tree() for _ in range(TREE_COUNT)]

        for _ in range(GENERATIONS):
            new_trees = []

            fitnesses = []
            for tree in trees:
                fitness = Evaluator.score(tree, data, node_var)
                fitnesses.append(fitness)
            fitnesses = np.array(fitnesses)
            fitnesses /= np.linalg.norm(fitnesses)

            while len(new_trees) <= TREE_COUNT:
                r = random()
                if r < PROB_POINT:
                    # Point mutation
                    candidate_tree = np.random.choice(trees, 1, p=fitnesses)
                    tree = Mutations.mutate_point(candidate_tree)
                    new_trees.append(tree)
                elif r < PROB_POINT + PROB_CROSSOVER:
                    # Crossover mutation
                    ctree1, ctree2 = np.random.choice(trees, 2, p=fitnesses)
                    tree1, tree2 = Mutations.mutate_crossover(ctree1, ctree2)
                    new_trees.append(tree1)
                    new_trees.append(tree2)
                else:
                    # Reproduction mutation
                    candidate_tree = np.random.choice(trees, 1, p=fitnesses)
                    tree = candidate_tree.deepcopy()
                    new_trees.append(tree)

        # Return trees
        scores = [Evaluator.score(tree, data, node_var) for tree in trees]
        best_tree = trees[np.argmax(scores)]
        return best_tree.collapse()

if __name__ == "__main__":
    #run()
    pass
