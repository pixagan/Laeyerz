from laeyerz.flow.Steps import Steps
from laeyerz.flow.Node import Node

class AgentState(Node):

    def __init__(self, name, config):
        super().__init__(name)

        self.name = name
        self.config = config
        self.state = {}
        self.steps = Steps()
        self.task = None
        self.plan = None


    def add_step(self, step):
        self.steps.add_step(step)

    def get_steps(self):
        return self.steps.get_steps()


    def get_state(self):
        return self.config.get("state")

    def set_state(self, state):
        self.config["state"] = state


    def set_task(self, task):
        self.task = task

    def update_plan(self, plan):
        self.plan = plan