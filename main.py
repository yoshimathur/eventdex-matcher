import pandas as pd
from data.data_center import DataCenter
from funcs.matcher import Matcher
from caller.client import OpenAI_Client
import json

data_center = DataCenter()
df = data_center.from_csv('data/test_seller_data.csv')

matcher = Matcher(df)
user_prompt = "Can you return all businesses involved in construction?"

parameters_completion = matcher.caller.get_parameters(
    input=user_prompt, 
    data_cols=list(matcher.df.columns)
)
print(parameters_completion)

if type(parameters_completion) == str: 
    # function not called response returned instead of parameters
    print(parameters_completion)
else: 
    cols = parameters_completion[0]
    keywords = parameters_completion[1]

    matches = matcher.find_matches(cols, keywords)

    print(matches)

# with open('caller/embedding_cache.json') as f: 
#     embedding_cache = json.load(f)
    
# for entry in embedding_cache['cache']: 
#     print(entry['col'])