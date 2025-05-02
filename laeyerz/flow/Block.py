class Block:

    def __init__(self, name, nodes, edges):
        self.name = name
        self.nodes = nodes
        self.edges = edges

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, edge):
        self.edges.append(edge)
