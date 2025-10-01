##-------- Accounting Assistant ---------

from laeyerz.flow.Agent import Agent


income_table  = []
expense_table = []

def income_tool(date, head, amount):

    income_table.append([head, amount])

    return "Income table updated"
    


def expense_tool(date, head, amount):

    expense_table.append([head, amount])

    return "Expense Table Updated"





tool1 = {
    "name":"expense_tool",
    "function":expense_tool,
    "inputs":[
        {"name":"date", "type": "string", "isRequired":True},
        {"name":"head", "type": "string", "isRequired":True},
        {"name":"amount", "type": "number", "isRequired":True}
    ],
}

tool2 = {
    "name":"income_tool",
    "function":income_tool,
    "inputs":[
        {"name":"date", "type": "string", "isRequired":True},
        {"name":"head", "type": "string", "isRequired":True},
        {"name":"amount", "type": "number", "isRequired":True}
    ],  
}

tools = [tool1, tool2]


#system prompt

instructions = """
    You are an accounting assistant. Classify the users query into an income and expense and use the relevant tool to update the relevant table.
"""


accounting_agent = Agent(
    name="Accounting Assistant",
    description="An accounting assistant that can classify the users query into an income and expense and use the relevant tool to update the relevant table.",
    llm_model = "gpt-4o-mini",
    tools=tools,
    instructions=instructions,
    
)

accounting_agent.run("I want to add 1000 to my income on 2024-01-01")

