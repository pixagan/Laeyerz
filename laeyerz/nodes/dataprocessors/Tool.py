# Copyright 2025 Pixagan Technologies
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Tool module for defining reusable tools
in the Laeyerz framework.
"""

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