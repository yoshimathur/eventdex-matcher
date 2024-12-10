import openai
import json

from caller.structured_outputs import QueryPairs

# OpenAI_Client class to create an easily accessible access point to OpenAI API 
# helps easily utilize 

class OpenAI_Client(): 

    api_key = "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"
    parameters_model = 'gpt-3.5-turbo'

    def __init__(self):
        self.client = openai.OpenAI(api_key=self.api_key)

    def create_embeddings(self, input): 
        response = self.client.embeddings.create(
            model="text-embedding-3-small",
            input=input
        )
        embedding = response.data[0].embedding
        return embedding
    
    def save_embedding(self, col, embedding): 
        # embedding cache for data col embeddings 
        with open('caller/embedding_cache.json') as f: 
            embedding_cache = json.load(f)
        print(embedding_cache)
        cache = embedding_cache['cache']

        entry = {
            "entry": {
                "col": col, 
                "embedding": embedding
            }
        }
        entry = json.dumps(entry)

        cache.push(entry)

        with open('caller/embedding_cache.json') as f: 
            json.dump()

    def unpack_parameters(self, pairs): 
        cols = []
        # keywords will be 2 dimensional
        keywords = []

        for pair in pairs['pairs']: 
            cols.append(pair['col'])
            keywords.append(pair['keywords'])

        return (cols, keywords)

    # despite strict enabled in matcher_tool openai response unstructured 
    def get_parameters(self, input, data_cols): 
        with open('caller/matcher_tool.json') as f: 
            matcher_tool = json.load(f)
        
        matcher_tool['parameters']['properties']['pairs']['items']['properties']['col']['enum'] = data_cols
        # structure output 
        struct_tool = openai.pydantic_function_tool(QueryPairs)

        tools = [{"type": "function", "function": matcher_tool}, struct_tool]
        messages = [
            {"role": "system", "content": "You are a helpful user assistant capable of answering user questions using your knowledge and the supplied tools. Use the supplied tools as needed."},
            {"role": "user", "content": f"{input}"}
        ]
        
        # save messages to append to later
        self.messages = messages

        response = self.client.chat.completions.create(
            model=self.parameters_model,
            messages=messages, 
            tools=tools
        )

        response_msg = response.choices[0].message

        if (response_msg.tool_calls == None): 
            return response_msg.content
        else: 
            tool_call = response_msg.tool_calls[0]
            args = json.loads(tool_call.function.arguments)
            return self.unpack_parameters(args)
