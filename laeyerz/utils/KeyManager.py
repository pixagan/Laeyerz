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
from pathlib import Path
import json
from dotenv import load_dotenv
from dotenv import dotenv_values
load_dotenv()



class KeyManager:
    
    def __init__(self, filename):
        print("Load API Keys")
        self.key_path = filename
        self.keys = {}

        keys_path = Path(filename).expanduser().resolve()
        if not keys_path.exists():
            raise FileNotFoundError(f"Key file not found: {keys_path}")

        if keys_path.suffix == ".env":
            keys = dotenv_values(keys_path)
        elif keys_path.suffix == ".json":
            with open(keys_path) as f:
                keys = json.load(f)
        else:
            raise ValueError("Unsupported key file type")

        self.keys = dict(keys)  # seal it


    def __getitem__(self, key: str) -> str:
        if key not in self.keys:
            raise KeyError(f"Missing key: {key}")
        return self.keys[key]


    def loadKeys(self):
        with open(self.key_path, 'r') as file:
            keys = json.load(file)
            self.keys = keys
        print("Keys")


    def get(self, key: str, default=None):
        return self._keys.get(key, default)


    def checkKeyExists(self, key):
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

     