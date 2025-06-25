class Prompt:

    def __init__(self, llm_model="gpt-4o-mini", system_prompt="You are a helpful assistant", instructions="Based on the query and any context provided provide the best possible answer."):
        print("Prompt")
        self.llm_model     = llm_model
        self.system_prompt = system_prompt
        self.instructions  = instructions


    def create_prompt(self, prompt_type, system_prompt, query, context, instructions):
        print("Creating Prompt")

        promptf = """



        """





#----------------------------------------------------------------------


def main():

    prompt = Prompt()
   

#----------------------------------------------------------------------

if __name__ == "__main__":
    main()


#----------------------------------------------------------------------






 