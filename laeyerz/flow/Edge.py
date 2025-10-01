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
Edge module for workflow edge management
in the Laeyerz framework.
"""


import uuid

class Edge:
    def __init__(self, source, target, label, condition=None):
        self.id = uuid.uuid4()
        self.source = source
        self.target = target
        self.label = label

        if condition is None:
            self.condition = lambda x: True
        else:
            self.condition = condition

    def __str__(self):
        return f"Edge(id={self.id}, source={self.source}, target={self.target}, label={self.label})"


    def evaluate(self, inputs, app_state):
        condition = self.condition(inputs)

        return condition

    def to_dict(self):
        return {
            "id": str(self.id),
            "source": self.source,
            "target": self.target,
            "label": self.label,
        }

        