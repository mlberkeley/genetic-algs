
from function import Function
from tree import Tree
from node import Node
from terminal import Terminal

class Initializer(object):
    @staticmethod
    def create_full_tree(depth):
        if depth == 0:
            terminal = Terminal.random_terminal()
            node = Node("terminal", terminal)
            return Tree(node)
        else:
            function = Function.random_function()
            root_node = Node("function", function)
            result = Tree(root_node)
            for _ in range(2):  #function.arity()
                result.add_child(Initializer.create_full_tree(depth - 1))
            return result

    @staticmethod
    def create_grow_tree(depth):
        # TODO
        return

if __name__ == "__main__":
    tree = Initializer.create_full_tree(2)
    print(tree)
