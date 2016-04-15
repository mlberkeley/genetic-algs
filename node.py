
class NodeType(object):
    """ Enum of node types """
    FUNCTION, TERMINAL = range(2)

class Node(object):
    def __init__(self, node_type, value):
        self.node_type = node_type
        self.value = value
