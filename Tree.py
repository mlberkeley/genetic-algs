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
        entry = self.node.Type + " " + str(self.node.value)
        if self.children:
            for i in range(len(self.children)):
                entry += "\n"
                entry += str(i) + ": " + str(self.children[i])

        return entry
