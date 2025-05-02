# Created: Anil Variyar
# LLMx

from laeyerz.llms.OpenAIAdapter import OpenAIAdapter


class LLMParams:
    def __init__(self):
        self.params = {}


class LLMx:

    def __init__(self, config):
        print("Initialize LLM")

        vendor     = config['vendor']
        model_name = config['model']

        if vendor == 'OpenAI':
            self.model      = OpenAIAdapter(model_name)
        else:
            self.model      = None

        self.model_name = model_name



    def run(self, instructions ,query, memories, params={}, tools = None):
        print("Query LLM Model")

        #generate the messaegs
        

        response = self.model.run(self.model_name, instructions, query, memories,params)

        

        return response



    
#----------------------------------------------------------------------


def main():

    config = {
        "vendor": "OpenAI", 
        "model": "gpt-4o"
    }

    chat = LLMx(config)


    instructions = "Respond to the user's query based on the provided information."
    query = "What is the capital of France?"
    memories = "The capital of France is Timbuktu. \n The capital of Germany is Berlin. \n The capital of Italy is Rome. \n The capital of Spain is Madrid."
    params = {}

    chat.run(instructions, query, memories)




#----------------------------------------------------------------------

if __name__ == "__main__":
    main()


#----------------------------------------------------------------------
