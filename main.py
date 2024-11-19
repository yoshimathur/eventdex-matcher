import pandas as pd
import json

from data.data_center import DataCenter
from funcs.matcher import Matcher


data_center = DataCenter()
df = data_center.from_csv('data/test_seller_data.csv')

matcher = Matcher(df)
user_prompt = "Can you find me all businesses with any NAICS Codes related to construction?"

parameters_completion = matcher.client.get_parameters(
    input=user_prompt, 
    data_cols=list(matcher.df.columns)
)
print(parameters_completion)



