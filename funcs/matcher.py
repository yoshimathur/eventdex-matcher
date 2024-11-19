import pandas as pd
import openai

from callers.client import OpenAI_Client

class Matcher(): 
    def __init__(self, df): 
        self.client = OpenAI_Client()
        self.df = df

    def find_matches(self, cols, keywords) -> list[int]: 
        # function to find matches using relevant columns (cols) and queried subjects (subs)
        # function returns a list of indices from the dataset of relevant matches to the query 
        if len(cols) != len(keywords): 
            return []
        
        for i, col in enumerate(cols): 
            data = self.df[col]
            data = data.dropna()

            key = keywords[i]

            for i, item in enumerate(data[col].iterrows()): 
                if str(item) in key: 
                    print(i)


            
                
