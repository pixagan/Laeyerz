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



class AppState:

    def __init__(self):

        self.state = {
            "app_state": "app_state",
            "Shared":{},
            "Inputs":{},
            "Outputs":{},
        }

    def add_section(self, node_id):
        self.state[str(node_id)] = {}

    def __str__(self):
        return f"AppState(state={str(self.state)})"


    def get_all(self):
        return self.state


    def get(self, section, key):

        result = {
        }

        key_out = section + ":" + key
        result[key_out] = self.state[section][key]
        return result


    def get_section(self, section):
        return self.state[section]


    # def get(self, labels=[]):   

    #     #if labels is a single value, push it into a string
    #     if isinstance(labels, str):
    #         labels = [labels]

    #     result = {}
    #     for label in labels:
    #         if label["node"] in self.state:
    #             if label["label"] in self.state[label["node"]]:
    #                 result[label["label"]] = self.state[label["node"]][label["label"]]

    #         # if label in self.state:
    #         #     result[label] = self.state[label]
    #     return result


    def update(self, node_id, label, value):
        self.state[str(node_id)][label] = value


    def delete_node(self, node_id):
        del self.state[str(node_id)]


    
def main():
    app_state = AppState()
    app_state.add_node("1")
    app_state.update("1", "test", "test")
    print(app_state.get("1", "test"))

if __name__ == "__main__":
    main()