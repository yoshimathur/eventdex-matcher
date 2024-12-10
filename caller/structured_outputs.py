from pydantic import BaseModel

# class Keywords(BaseModel): 
#     keyword_1: str
#     keyword_2: str
#     keyword_3: str
#     keyword_4: str
#     keyword_5: str

class QueryPair(BaseModel): 
    col: str
    keywords: list[str]

class QueryPairs(BaseModel): 
    pairs: list[QueryPair]
