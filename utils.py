"""
A place for general helper functions.
"""

import json
import re
import time


def cool_off(func, arg1, arg2, arg3, arg4):
    """Take a set of incremental time-outs from function"""
    attempts = 0
    while True:
        result = func(arg1, arg2, arg3, arg4)
        if result is None:
            attempts += 1
            print(f"Going to sleep for {attempts} seconds")
            time.sleep(attempts)
        else:
            return result


def export_to_jsonl(data:list[dict], filename:str="dataset.jsonl") -> None:
    with open(filename, 'w', encoding='utf-8') as f:
        for entry in data:
            json_line = json.dumps(entry, ensure_ascii=False)
            f.write(json_line + '\n')


def extract_text(output:str, symbol:str) -> list:
    """Extract text from an output string."""
    return re.findall(f"<<{symbol}>>(.*?)<</{symbol}>>", output, re.DOTALL)


def read_txt_file(filename:str) -> str:
    """Wrapper function to read text file"""
    with open(filename, 'r') as file:
        return file.read()


def split_into_chunks(text:str, max_tokens:int=1_000_000, token_approx=4) -> list:
    # Used ChatGPT to write it
    """Split text into chunks under the token limit. Assumes ~4 characters per token."""
    max_chars = max_tokens * token_approx
    return [text[i:i + max_chars] for i in range(0, len(text), max_chars)]
