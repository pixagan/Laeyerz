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
ToolWrapper module for wrapping external tools
in the Laeyerz framework.
"""
import inspect
from typing import Any, Dict



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




def tool_parse(func) -> Dict[str, Any]:
    source = inspect.getsource(func)
    tree   = ast.parse(source)
    node   = tree.body[0]


    name   = node.name

    params = []
    if isinstance(node, ast.FunctionDef):
        print("functions : ", node.name, node.args, node.returns)
        for arg in node.args.args:
            default = None
            if node.args.defaults:
                defaults = node.args.defaults
                default_offset = len(node.args.args) - len(defaults)
                if node.args.args.index(arg) >= default_offset:
                    default = ast.unparse(defaults[node.args.args.index(arg) - default_offset])
            arg_type = ast.unparse(arg.annotation) if arg.annotation else None
            params.append({
                "name": arg.arg,
                "description":arg.arg,
                "type": arg_type,
                "default": default,
                "isRequired":True
            })


    print("Returns : ",ast.unparse(node.returns))

    print("Docstring : ", ast.get_docstring(node))

    
    # Extract return type
    returns = ast.unparse(node.returns) if node.returns else None

    # Extract docstring
    docstring = ast.get_docstring(node)

    print(name)

    tool = tool_wrapper(name, docstring, params)

    print("Tool : ", tool)

    
    return {
        "name": name,
        "params": params,
        "returns": returns,
        "description": docstring,
    }
        