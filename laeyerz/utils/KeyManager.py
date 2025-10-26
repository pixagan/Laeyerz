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
KeyManager module for API key management
in the Laeyerz framework.
"""

import os
from dotenv import load_dotenv
load_dotenv()



class KeyManager:
    
    def __init__(self, key_path):
        print("Load API Keys")
        self.key_path = key_path

        self.keys = {}


    def loadKeys(self):
        with open(self.key_path, 'r') as file:
            keys = json.load(file)
            self.keys = keys
        print("Keys")


    def checkKey(self, key):
        if key in self.keys:
            return self.keys[key]
        else:
            return None


    def check_validity(self, key):
        if key in self.keys:
            return True
        else:
            return False


        



#----------------------------------------------------------------------


def main():

 
    km = KeyManager()


   


#----------------------------------------------------------------------

if __name__ == "__main__":
    main()


#----------------------------------------------------------------------

     