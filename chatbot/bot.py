import os

import openai

# openai.api_key = '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'


def ask(question):
    
    response = openai.Completion().create(
        prompt=question, 
        engine="text-davinci-002", 
        temperature=0,
        top_p=1, 
        # frequency_penalty=0, 
        # presence_penalty=0.4, 
        
        max_tokens=30)
    answer = response
    print(answer)
    return answer

# que = ''
# while que != 'q':

#     que = str(input('Que : '))

#     ask(que)
# else:
#     exit()

