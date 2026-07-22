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

class Steps:

    def __init__(self):
        self.steps = []

    def add_step(self, step):
        self.steps.append(step)

    def get_steps(self):
        return self.steps

    def get_step(self, index):
        return self.steps[index]

    def get_current_state(self):
        current_state = []
        
        return self.steps