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
LocalDB module for local database operations
in the Laeyerz framework.
"""
import uuid

class LocalDB(Node):
    def __init__(self, dbname="Local Python DB", schema_in={}):
        self.dbname = dbname
        self.schema = {"id":"uuid"}
        self.nItems = 0
        self.items  = []
        self.map = {}

        for key, value in schema_in.items():
            self.schema[key] = value


    def update_schema(self, schema):
        self.schema = schema


    def validate_entry(self, item):
        for key, value in item:
            if key not in self.schema.keys():
                return False
            if type(item[key]) != self.schema[key]:
                return False
        return True

    def add_item(self, item):
        validated = self.validate_entry(item)
        if validated:
            item["id"] = str(uuid.uuid4())
            self.items.append(item)
            self.map[item["id"]] = item
            self.nItems += 1
        else:
            raise ValueError("Invalid entry")

    def remove_item(self, item_id):
        self.items.remove(self.map[item_id])
        self.nItems -= 1
        del self.map[item_id]

    def update_item(self, item_id, name, value):
        self.items[self.map[item_id]][name] = value

    def get_nItems(self):
        return self.nItems

    def get_item_byId(self, item_id):
        return self.map[item_id]

    def get_all(self):
        return self.items

    def search(self, key, value):
        """
        Search for items where the specified key contains a string or substring that matches the value.
        
        Args:
            key (str): The key to search in
            value (str): The string to search for
            
        Returns:
            list: List of items that match the search criteria
        """
        matching_items = []
        
        for item in self.items:
            if key in item:
                item_value = str(item[key]).lower()
                search_value = str(value).lower()
                
                if search_value in item_value:
                    matching_items.append(item)
        
        return matching_items

    


def laeyerzdb_function(inputs):
    """Sqlite function that processes inputs and returns output"""
    # Extract inputs - you can customize this based on your needs
    text = inputs.get('text', '')
    model = inputs.get('model', 'gpt-3.5-turbo')
    
    # Placeholder for OpenAI API call
    # In a real implementation, you would call the OpenAI API here
    response = f"Sqlite processed: {text} using {model}"
    
    return {"output": response}


def create_laeyerzdb_node(node_name):
    """Factory function to create and return an SqliteNode"""
    # Create the SqliteNode with proper initialization
    LaeyerzDBNode = Node(
        node_type='LaeyerzDB',
        node_subtype='Local DB',
        node_name=node_name,
        description='Node for Sqlite API interactions'
    )

    # Set the function and configure inputs/outputs
    LaeyerzDBNode.action = 'LaeyerzDB LLM call'
    LaeyerzDBNode.set_function(laeyerzdb_function)
    LaeyerzDBNode.inputs = ['text', 'model']  # Expected input parameters
    LaeyerzDBNode.outputs = ['output']  # Expected output parameters
    
    return LaeyerzDBNode


# Create a default instance
#OpenAINode = create_openai_node()


# Return the configured node
if __name__ == "__main__":
    # For testing the node
    from laeyerzflow.flow.AppState import AppState
    
    app_state = AppState()
    app_state.update('text', 'Hello from OpenAI!')
    app_state.update('model', 'gpt-4')
    
    # result, next_node = OpenAINode.run(app_state)
    # print(f"Result: {result}")
    # print(f"Next node: {next_node}")






