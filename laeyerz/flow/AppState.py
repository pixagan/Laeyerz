class AppState:

    def __init__(self):
        self.state = {}

    def get_params(self, params):

        return {key: self.state[key] for key in params if key in self.state}

    def set_state(self, input_tag, input_value):

        #self.state = {}
        self.state[input_tag] = input_value


    def clear_state(self, node_id):
        self.state[node_id] = {}



# ------------------------------------------------------------------

def main():

    appstate = AppState()
    
    appstate.set_state("1", "input", "Hello, world!")
    
    print(appstate.get_state("1"))


#----------------------------------------------------------------------

if __name__ == "__main__":
    main()


#----------------------------------------------------------------------

