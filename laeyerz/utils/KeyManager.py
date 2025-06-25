# Created: Anil Variyar
# Key Manager, check if keys exist, Does not store any keys in memory

import os
from dotenv import load_dotenv
load_dotenv()



class KeyManager:
    
    def __init__(self):
        print("Load API Keys")
        self.keys = {}


    def loadKeys(self):
        print("Keys")


    def checkKey(self, key):
        if key in self.keys:
            return self.keys[key]
        else:
            return None


    def check_validity(self, key):
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

     