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

