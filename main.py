import pandas as pd
import json
from funcs.matcher import Matcher

matcher = Matcher('data/test_seller_data.csv')

# print(matcher.df.dtypes)
# matcher.find_matches(cols=['Keywords'], subs=['finance'])

parameters_completion = matcher.client.getParameters(
    input="Can you provide me with all companies that have NAICS codes related to construction?", 
    data_cols=list(matcher.df.columns)
)
print(parameters_completion)

