class Tool:
    def __init__(self, name, description, function):
        self.name = name
        self.description = description
        self.function = function

    def evaluate(self, query):
        return self.function(query)