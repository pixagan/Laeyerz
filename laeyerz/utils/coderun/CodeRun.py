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
CodeRun module for code execution
in the Laeyerz framework.
"""
import subprocess
import sys

def code_run(code, params):
    try:
        # Run code in a subprocess to isolate execution
        with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as tmp:
            tmp.write(code.encode("utf-8"))
            tmp.flush()
            result = subprocess.run(
                [sys.executable, tmp.name],
                capture_output=True,
                text=True,
                timeout=5
            )
        return {
            "stdout": result.stdout,
            "stderr": result.stderr
        }
    except subprocess.TimeoutExpired:
        return {"stdout": "", "stderr": "Execution timed out"}
    except Exception as e:
        return {"stdout": "", "stderr": str(e)}




def main():
    code = """print('Hello, World!')"""
    params = {}
    result = code_run(code, params)
    print(result)

if __name__ == "__main__":
    main()