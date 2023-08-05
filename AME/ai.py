import openai
import os
from dotenv import load_dotenv


load_dotenv()
openai.api_key = os.getenv('OPENAI_API')

def text(inp: str, p:str, l:str):
    if int(l) > 900:
        return "Word limit exceeded!"
    temp = inp
    inp = "Level:" + p + "\nWord Limit (strict):" + l + "\n\n"
    inp += temp
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {
                'role':'user',
                'content':inp
            },
        ],
    )
    return response['choices'][0]['message']['content']
