class MemoryLayer:

    def __init__(self):
        self.memory = {}
        self.sources = []
        

    def add_memory(self, memory):
        self.memory[memory.id] = memory