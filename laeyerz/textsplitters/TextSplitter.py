# Created: Anil Variyar
# Text Splitter

import re
from typing import List



class TextSplitter:

    def __init__(self):
        print("Splitting the Text for Vectorization")
        self.tokenizer = None
        self.max_tokens = 512


    def run(self, text):
        print("Split")

        
        max_tokens = self.max_tokens
        tokenizer  = self.tokenizer

       
        # Regex to match paragraphs
        paragraphs = re.findall(r'(.*?)(\r?\n\r?\n|$)', text, re.DOTALL)

        # Extract and clean paragraphs (ignoring the newline separators)
        paragraphs = [p[0].strip() for p in paragraphs if p[0].strip()]

        chunks = paragraphs

        print("nChunks : ", len(chunks))


        return chunks



