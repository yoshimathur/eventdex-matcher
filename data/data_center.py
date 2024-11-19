import pandas as pd 

class DataCenter(): 
    def __init__(self): 
        pass

    def from_csv(self, filename): 
        df = pd.read_csv(filename)

        return df