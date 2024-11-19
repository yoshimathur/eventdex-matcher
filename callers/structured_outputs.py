from pydantic import BaseModel

class QueryPair(BaseModel): 
    col: str
    keywords: list[str]

class QueryPairs(BaseModel): 
    pairs: list[QueryPair]
