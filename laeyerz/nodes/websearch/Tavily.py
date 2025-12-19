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
Tavily module for Tavily web search operations
in the Laeyerz framework.
"""

import json
from tavily import TavilyClient 
from laeyerz.flow.Node import Node


class TavilyNode(Node):
    def __init__(self, node_name, config={}, description="Run websearch with Tavily"):
        super().__init__(node_name=node_name, description=description)
        self.metadata = {
            "node_type": "WebSearch",
            "node_subtype": "Tavily",
        }
        self.view = {
            "view_type": "WebSearch",
            "view_subtype": "Tavily",
        }

        self.client = TavilyClient(config.get('api_key'))
        


    def search(self, query):
        response = self.client.search(
            query=query
        )

        return response



def main():

    tavily = TavilyNode("TavilyTest")
    searchResults = tavily.search("The latest goal tally of Cristiano Ronaldo")
    print(searchResults)
    

if __name__ == "__main__":
    main()