# Created: Anil Variyar
# CSV Loader

import pandas as pd

class CSVReader:

    def __init__(self):
        print("Loading CSV")


    def run(self, filename):
        print("")

        data = pd.read_csv(filename)

        return data