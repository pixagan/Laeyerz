
class Edge:
    def __init__(self, node_0, node_1, condition=None):
        self.node_0 = node_0
        self.node_1 = node_1
        self.condition = condition


    def check_condition(self):
        
        if self.condition is None:
            return True
        else:
            return self.condition.evaluate()



