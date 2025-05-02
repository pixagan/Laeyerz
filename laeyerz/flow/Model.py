# A dummy model class that you can test the flow with or extend to add your own modules

class Model:

    def __init__(self, name, config=None):
        self.name = name
        self.config = config
       

    def evaluate(self, input):

        print("Evaluating Model : ", self.name)

        return self.name

