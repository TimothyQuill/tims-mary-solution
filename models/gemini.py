"""
This script handles all the Gemini API logic
"""

from google import genai
from google.genai import types
from os import environ

import utils


client = genai.Client(
    api_key=environ.get('GEMINI_KEY')
)


def _completion(prompt:str, model:str, temperature:float, top_p:float) -> str:
    """Wrapper function to get completions from Gemini API"""
    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=temperature,
            top_p=top_p
        )
    )

    return response.text


def completion(prompt:str, model:str="gemini-2.5-flash", temperature:float=1., top_p:float=.9) -> list:
    return utils.cool_off(_completion, prompt, model, temperature, top_p)
