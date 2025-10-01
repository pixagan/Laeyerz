# Copyright (c) 2025 Pixagan Technologies
#
# Licensed under the BSD License. See LICENSE file in the project root for
# full license information.

"""
LDocument module for document processing and vectorization
in the Laeyerz framework.
"""


import os
import numpy as np
import fitz


from dotenv import load_dotenv
load_dotenv()

from laeyerz.utils.textsplitters.TextSplitter import TextSplitter


class LDocument:

    def __init__(self, memory = None):
        print("Memory X")
        self.filename  = None
        self.doc_pages = None
        self.memory    = memory


    def load_pdf(self, filename):
        print("Loading PDF")

        self.filename = filename

        doc = fitz.open(filename)
        doc_pages = []

        for page_num, page in enumerate(doc, start=1):
            blocks = page.get_text("blocks")  # Extract text blocks

            blocks.sort(key=lambda b: (b[1], b[0]))  # Sort blocks by vertical (y), then horizontal (x) positions

            # Estimate median X position to identify columns
            x_coords = [block[0] for block in blocks]
            median_x = (max(x_coords) + min(x_coords)) / 2

            left_column = []
            right_column = []

            for block in blocks:
                x0, y0, x1, y1, text, _, _ = block
                if x0 < median_x:
                    left_column.append((y0, text))
                else:
                    right_column.append((y0, text))

            # Sort each column vertically
            left_column.sort()
            right_column.sort()

            # Combine columns: left first, then right
            page_text = [text for _, text in left_column + right_column]

            doc_pages.append({
                "page": page_num,
                "content": "\n".join(page_text)
            })

        self.doc_pages = doc_pages

        return doc_pages



    def into_chunks(self, doc=None):
        print("Into Chunks")

        if(doc is None):
            doc = self.doc_pages


        splitter = TextSplitter()

        document_chunks = []

        for iP in range(0, len(doc)):
            text = doc[iP]['content']
            chunks = splitter.run(text)
            formatted_chunks = [{"text": chunk} for chunk in chunks]
            
            document_chunks.extend(formatted_chunks)

            print("Page : ", iP, "--------------------------------")
            print(len(document_chunks))

        return document_chunks




    def add(self, document, document_type):
        print("Adding document")

        items = None
        with open(filename, 'r') as file:
            items = json.load(file)

        if(items):
            self.memory.add_document(items, document_type)






    def chat(self, text_in):
        print("Searching Agent Memory")

        #get memories from document
        mem_out = self.memory.search(text_in)

        response = None

        return response


    def export_file(self, filename):
        print("Export File")




#----------------------------------------------------------------------




def main():

    document1 = LDocument()
    structured_data = document1.load_pdf("../datasets/AR_1.pdf")
   
    

    splitter = TextSplitter()
    sentences = splitter.into_sentences(structured_data[0]['content'])
  

#----------------------------------------------------------------------

if __name__ == "__main__":
    main()


#----------------------------------------------------------------------

     