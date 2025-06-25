def tool_wrapper_openai(tool_name, description, properties, output):

    tool = {
        "type": "function",
        "function": {
            "name": tool_name,
            "description": description,
            "parameters": {
                "type": "object",
                "properties": {
                },
                "required": []
            }
        }
    }

    for property in properties:
        tool["function"]["parameters"]["properties"][property["name"]] = {"type": property["type"], "description": property["description"]}
        if(property["isRequired"] == True):
            tool["function"]["parameters"]["required"].append(property["name"]) 


    return tool