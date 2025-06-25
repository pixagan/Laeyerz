class Tool:
    def __init__(self, name, description, parameters):
        self.name = name
        self.description = description
        self.function = function

        {
        "type": "function",
        "function": {
            "name": "weather_tool",
            "description": "Get the current temperature in a city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "Name of the city (e.g., Delhi, Paris)"
                    }
                },
                "required": ["location"]
            }
        }
        }

    def evaluate(self, query):
        return self.function(query)