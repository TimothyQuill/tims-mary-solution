"""
This script handles all the ChatGPT API logic
"""

from openai import OpenAI
from os import environ

import utils


client = OpenAI(
    api_key=environ.get('OPENAI_KEY'),
)


def _completion(prompt:str, model:str, temperature:float, top_p:float) -> str:
    """Wrapper function to get completions from ChatGPT API"""
    response = client.responses.create(
        model=model,
        input=prompt,
        temperature=temperature,
        top_p=top_p
    )

    return response.output_text


def completion(prompt:str, model:str="gpt-4.1-mini", temperature:float=1., top_p:float=.9) -> list:
    return utils.cool_off(_completion, prompt, model, temperature, top_p)
