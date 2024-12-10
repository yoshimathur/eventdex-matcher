import pandas as pd
import numpy as np
from scipy.spatial import distance

from caller.client import OpenAI_Client

class Matcher(): 
    def __init__(self, df): 
        self.caller = OpenAI_Client()
        self.df = df

    def find_matches(self, cols, keywords): 
        # function to find matches using relevant columns (cols) and queried subjects (subs)
        # function returns a similarity-sorted list of indices from the dataset of relevant matches to the query 
        if len(cols) != len(keywords): 
            return []
        
        for i, col in enumerate(cols): 
            # .head() to limit api tokens for testing purposes -> delete later 
            data = self.df[col].head()
            keys = keywords[i]
            key_str = " ".join(keys)

            # search cache for data embedding otherwise create it
            data_embeddings = self.caller.get_embedding(col)
            if (not data_embeddings): 
                data_embeddings = data.apply(lambda x: self.caller.create_embeddings(str(x)))
                self.caller.save_embedding(col, list(data_embeddings))
            
            key_embedding = self.caller.create_embeddings(key_str)

            for data_embedding in data_embeddings: 
                sim = np.dot(key_embedding, data_embedding)
                print(sim)
                

