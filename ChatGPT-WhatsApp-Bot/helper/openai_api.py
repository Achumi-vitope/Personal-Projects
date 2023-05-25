import os
import openai
from dotenv import load_dotenv
load_dotenv()


openai.api_key = os.getenv('OPENAI_API_KEY')


def text_complition(prompt: str) -> dict:
    '''
    Call Openai API for text completion

    Parameters:
        - prompt: user query (str)

    Returns:
        - dict
    '''
    
    try:
        msg = "ᶜʰᵃᵗᴳᴾᵀ ᵇᵃˢᵉᵈ ᵂʰᵃᵗˢᵃᵖᵖ ᴮᵒᵗ ᵇʸ ⱽⁱᵗᵒᵖᵉ ᴬᶜʰᵘᵐⁱ"
        response = openai.Completion.create(
            model='text-davinci-003',
            prompt=f'Human: {prompt}\nAI:',
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=['Human:', 'AI:']
        )
        print("--------------\n",prompt)
        return {
            'status': 1,
            'response':msg + '\n\n' + response['choices'][0]['text'],
        }
    except:
        return {
            'status': 0,
            'response': 'Server is down.'
        }
        
