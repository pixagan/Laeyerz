from laeyerz.connectors.vectorstores.FAISSAdapter import FaissAdapter

class AgentMemory:

    def __init__(self):
        print("Agent Memory")

        self.memory = FAISSAdapter()


    def store(self):
        print("Adding to Memory")


    def recall(self):
        print("Recalling Memory")


    def update(self):
        print("Updating Memory")
        


class AgentMemoryST:

    def __init__(self):
        print("Agent Memory")

        self.memory = []


    def store(self):
        print("Adding to Memory")


    def recall(self):
        print("Recalling Memory")


    def update(self):
        print("Updating Memory")