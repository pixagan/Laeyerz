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

from collections.abc import Mapping
from dataclasses import is_dataclass, asdict

def dictify(func, output_keys=None):
    def wrapper(**kwargs):
        result = func(**kwargs)

        # Case 1: Already a mapping
        if isinstance(result, Mapping):
            return dict(result)

        # Case 2: Dataclass
        if is_dataclass(result):
            return asdict(result)

        keys = list(output_keys) if output_keys else []

        # Case 3: Tuple or List (multi-output)
        if isinstance(result, (tuple, list)):
            outputs = list(result)
            out = {}

            for i, value in enumerate(outputs):
                if i < len(keys):
                    out[keys[i]] = value
                else:
                    out[f"output_{i}"] = value

            return out

        # Case 4: Single value
        if keys:
            return {keys[0]: result}

        return {"output_0": result}

    return wrapper



def main():
    def test_function():
        #return {"name": "John", "age": 30}
        return 30

    function2 = dictify(test_function, [])
    outputs = function2()
    print(outputs)

if __name__ == "__main__":
    main()