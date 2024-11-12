import pandas as pd

from funcs.matcher import Matcher

matcher = Matcher('data/test_seller_data.csv')

print(matcher.df.dtypes)

matcher.find_matches(cols=['Keywords'], subs=['finance'])