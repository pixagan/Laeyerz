class ChatInput:

    def __init__(self):
        self.input_type = "chat"

    def evaluate(self):
        return input("Enter a message: ")


