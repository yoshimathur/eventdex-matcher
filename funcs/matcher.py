import pandas as pd
import numpy as np
import sklearn.metrics.pairwise as sci
import openai

from caller.client import OpenAI_Client

class Matcher(): 
    def __init__(self, df): 
        self.openai_client = OpenAI_Client()
        self.df = df

    def find_matches(self, cols, keywords) -> list[int]: 
        # function to find matches using relevant columns (cols) and queried subjects (subs)
        # function returns a list of indices from the dataset of relevant matches to the query 
        if len(cols) != len(keywords): 
            return []
        
        for i, col in enumerate(cols): 
            data = self.df[col]
            keys = keywords[i]
            key_str = " ".join(keys)

            data_embedding = data.apply(lambda x: self.client.create_embeddings(x))
            key_embedding = self.openai_client.create_embeddings(key_str)

            print(type(data_embedding), type(key_embedding))