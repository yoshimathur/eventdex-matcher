import openai
import json

# OpenAI_Client class to create an easily accessible access point to OpenAI API 
# helps easily utilize 

class OpenAI_Client(): 

    api_key = "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"
    parameters_model = 'gpt-3.5-turbo'

    def __init__(self):
        self.client = openai.OpenAI(api_key=self.api_key)

    def createEmbeddings(self, input): 
        self.client.embeddings.create(
            model="text-embedding-3-small",
            input=input, 
            embedding_format ="float"
        )

    def getParameters(self, input, data_cols): 
        with open('callers/matcher_tool.json') as f: 
            matcher_tool = json.load(f)
        
        matcher_tool['parameters']['properties']['cols']['enum'] = data_cols

        tools = [{"type": "function", "function": matcher_tool}]
        messages = [
            {"role": "system", "content": "You are a helpful user assistant capable of answering user questions using your knowledge and the supplied tools. Use the supplied tools more often than not."},
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
            return args
            # return (args['cols'], args['subs'])
