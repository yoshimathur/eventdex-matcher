import pandas as pd
import json

from data.data_center import DataCenter
from funcs.matcher import Matcher
from caller.client import OpenAI_Client

# data_center = DataCenter()
# df = data_center.from_csv('data/test_seller_data.csv')

# matcher = Matcher(df)
# user_prompt = "Can you return all businesses with representatives whose name has the letter 'A'?"

# parameters_completion = matcher.client.get_parameters(
#     input=user_prompt, 
#     data_cols=list(matcher.df.columns)
# )
# print(parameters_completion)

# if type(parameters_completion) == str: 
#     # function not called response returned instead of parameters
#     print(parameters_completion)
# else: 
#     cols = parameters_completion[0]
#     keywords = parameters_completion[1]

#     matcher.find_matches(cols, keywords)

col = 'Random col'
embedding = ['hi', 'bye', 'test']
OpenAI_Client().save_embedding(col, embedding)