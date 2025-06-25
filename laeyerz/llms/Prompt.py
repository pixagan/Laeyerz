class Prompt:
    def __init__(self):
        self.prompt = ""

    def construct_prompt(self, inputs):

        #instructions
        instructions = inputs["Instructions"]
        #context - memories
        memories = inputs["Memories"]
        #query
        query = inputs["Query"]
        

        return self.prompt


    def evaluate(self):
        return self.construct_prompt()

