class Steps:

    def __init__(self):
        self.steps = []

    def add_step(self, step):
        self.steps.append(step)

    def get_steps(self):
        return self.steps

    def get_step(self, index):
        return self.steps[index]

    def get_current_state(self):
        current_state = []
        
        return self.steps