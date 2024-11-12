import pandas as pd 

class Data_Converter_CSV(): 
    def __init__(self, f): 
        self.file = f
        self.df = pd.read_csv(f, on_bad_lines='skip')