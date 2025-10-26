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
DocLoad module for document loading operations
in the Laeyerz framework.
"""
from laeyerz.flow.Node import Node

class DocLoad(Node):

    def __init__(self):
        print("Loading Doc")

    def load_doc(self, filename):
        print("Loading Doc")

        """
        Load and read a DOCX file
        Args:
            file_path (str): Path to the DOCX file
        Returns:
            str: Text content of the document
        """
        try:

            doc = Document(file_path)
            full_text = []
            
            # Extract text from paragraphs
            for para in doc.paragraphs:
                if para.text.strip():  # Only add non-empty paragraphs
                    full_text.append(para.text)
                    
            return '\n'.join(full_text)
            
        except ImportError:
            print("Please install python-docx: pip install python-docx")
            return None
        except Exception as e:
            print(f"Error loading document: {str(e)}")
            return None





