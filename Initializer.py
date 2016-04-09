from Function import Function
from Tree import Tree
from Node import Node
from Terminal import Terminal

class Initializer:

    def create_full_tree(depth):
        if depth == 0:
            terminal = Terminal.random_terminal()
            node = Node("terminal", terminal)
            return Tree(node)
        else:
            function = Function.random_function()
            root_node = Node("function", function)
            result = Tree(root_node)
            for i in range(2):  #function.arity()
                result.add_child(Initializer.create_full_tree(depth - 1))
            return result


    def create_grow_tree(depth):
        return

    def main():
        tree = Initializer.create_full_tree(2)
        print(tree)


Initializer.main()
