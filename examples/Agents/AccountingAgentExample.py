##-------- Accounting Assistant ---------


income_table  = []
expense_table = []

def income_tool(date, head, amount):

    income_table.append([head, amount])

    return "Income table updated"
    


def expense_tool(date, head, amount):

    expense_table.append([head, amount])

    return "Expense Table Updated"



#Tool descripitons
tools = [
    {
        "type":"function",
        "function":{
        "name": "income_tool",
        "description": "Updates the income table",
            "parameters": {
                "type": "object",
                "properties": {
                    "date": {"type": "string"},
                    "head": {"type": "string"},
                    "amount": {"type": "number"}
                },
                "required": ["date", "head", "amount"]
            }
        }
    },
    {
        "type":"function",
        "function":{
            "name": "expense_tool",
            "description": "Updates the expense table",
            "parameters": {
                "type": "object",
                "properties": {
                    "date": {"type": "string"},
                    "head": {"type": "string"},
                    "amount": {"type": "number"}
                },
                "required": ["date", "head", "amount"]
            }
        }
    }
]



#system prompt

system_prompt = """
    You are an accounting assistant. Classify the users query into an income and expense and use the relevant tool to update the relevant table.
"""


#Accounting Asistant

def accounting_assistant(query):

    #--- First LLM call ---------------------------------------------------------------------------------
    
    initial = client.chat.completions.create(
        model=model,
        messages =  [
            {"role":"system", "content":system_prompt},
            {"role":"user", "content":query}
        ],
        tools = tools,
        tool_choice = "auto"
    )

    message     = initial.choices[0].message
    tool_calls  = initial.choices[0].message.tool_calls
    id          = tool_calls[0].id
    tool_name   = tool_calls[0].function.name
    arguments   = json.loads(tool_calls[0].function.arguments)

    

    #-- Tool call -----------------------------------------------------------------------------------------
    
    tool_output = ""
    if(initial.choices[0].finish_reason == "tool_calls"):
        
        if(tool_name == tool_calls[0].function.name == "income_tool"):
            tool_output = income_tool(**arguments)
        elif(tool_name == tool_calls[0].function.name == "expense_tool"):
            tool_output = expense_tool(**arguments)

    else:
        print("Response : ",message = initial.choices[0].message)
        

        
    #--- Second LLM call -----------------------------------------------------------------------------------

    followup = client.chat.completions.create(
        model=model,
        messages = [
        {"role": "user", "content": query},
        initial.choices[0].message,
        {
            "role": "tool",
            "tool_call_id": id,
            "name": tool_name,
            "content": str(tool_output)
        }]
    )

    #--------- Final Response ------------------------------------------------------------------------------
    
    print("Response : ",followup.choices[0].message.content)
    
        




#Main

if __name__ == "__main__":

    accounting_assistant("I want to add 1000 to my income on 2024-01-01")