import pandas as pd

from data.data_converter_csv import Data_Converter_CSV

class Matcher(): 
    def __init__(self, f): 
        self.df = Data_Converter_CSV(f).df

    def find_matches(self, cols, subs) -> list[int]: 
        # function to find matches using relevant columns (cols) and queried subjects (subs)
        # function returns a list of indices from the dataset of relevant matches to the query 
        if len(cols) != len(subs): 
            return []
        
        for i, col in enumerate(cols): 
            data = self.df[col]
            data = data.dropna()

            subject = subs[i]

            
                
