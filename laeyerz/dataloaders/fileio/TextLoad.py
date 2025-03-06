# Created: Anil Variyar
# Text Loader

import os



class TextLoad:

    def __init__(self):
        print("Loading Text")



    # Extract =text using PyPDF
    def load_file(self, file_path):

        text = None

        with open(file_path, "r") as file:
            text = file.read()  # Returns a list of lines
        
        
        

        lines = text.split("\n")

        print(lines)

        




#----------------------------------------------------------------------



def main():

    filename = 'Swiggy_Sample.txt'
    tl = TextLoad()
    text = tl.load_file(filename)

    print("Text : ", text)
    



#----------------------------------------------------------------------

if __name__ == "__main__":
    main()


#----------------------------------------------------------------------

     