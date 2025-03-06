# Created: Anil Variyar
# Document

import os
import numpy as np


from dotenv import load_dotenv
load_dotenv()



class Document:

    def __init__(self, memory):
        print("Memory X")
        self.title  = None
        self.memory = memory


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

    document1 = Document()
   
    



#----------------------------------------------------------------------

if __name__ == "__main__":
    main()


#----------------------------------------------------------------------

     