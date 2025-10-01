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

class Tavily(Node):
    def __init__(self, node_name, description=""):
        super().__init__(node_name=node_name, description=description)
        self.api_key = api_key
        self.metadata = {
            "node_type": "WebSearch",
            "node_subtype": "Tavily",
        }
        self.view = {
            "view_type": "WebSearch",
            "view_subtype": "Tavily",
        }


    def search(self, query):
        pass



def main():

    tavily = Tavily("tavily_api_key")
    tavily.search("Hello, how are you?")

    

if __name__ == "__main__":
    main()