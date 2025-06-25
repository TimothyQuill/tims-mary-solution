"""
This script defines the logic to generate synthetic legal data.
"""

from prompts import prompts

import models.chatgpt as gpt
import models.gemini as gem
import utils


MODEL_TOKEN_LIMITS = {
    "gem": 1_000_000,   # gemini-2.5-flash
    "gpt": 200_000,     # gpt-4.1-mini
}


class DataGenerator:

    def __init__(self, data_file:str, model:str='gem'):
        self.token_limit = MODEL_TOKEN_LIMITS[model]
        self.dataset = []
        self.model = gem if model == 'gem' else gpt
        # Break the file into chunks, so it doesn't exceed the model window size
        self.chunked_text = utils.split_into_chunks(
            utils.read_txt_file(data_file),
            max_tokens=self.token_limit
        )

    def extract_queries(self, output:str, chunk_n:int) -> None:
        """Extract all queries from the model output"""
        queries = utils.extract_text(output, "Q")
        for q in queries:
            self.dataset.append({
                "chunk_n": chunk_n, # Will be used in the label creation phase
                "query": q.strip()
            })

    def extract_label(self, row_n:int, output:str) -> None:
        """Extract all queries from the model output"""
        chain_of_thought, _ = output.split("<<S>>")
        search_method = utils.extract_text(output, "S")[0]
        query = utils.extract_text(output, "Q")[0]
        self.dataset[row_n]["tools"] = [{
            "cot":      chain_of_thought,
            "name":     search_method,
            "query":    query.strip(),
        }]

    def generate_queries(self) -> None:
        """Generates a list of queries"""
        # Process each chunk, one-by-one
        for i, chunk in enumerate(self.chunked_text):
            prompt = prompts["generate-query"].format(chunk)
            output = self.model.completion(prompt, temperature=1.2)
            self.extract_queries(output, i)

    def generate_labels(self) -> None:
        """Generates a list of queries"""
        for row_n in range(len(self.dataset)):
            prompt = prompts["generate-label"].format(
                self.dataset[row_n]["query"],
                self.chunked_text[self.dataset[row_n]["chunk_n"]]
            )
            output = self.model.completion(prompt, temperature=0.)
            self.extract_label(row_n, output)
            # Finally, remove the chunk_n key from the row
            self.dataset[row_n].pop("chunk_n")

    def generate(self) -> None:
        self.generate_queries()
        self.generate_labels()
        utils.export_to_jsonl(self.dataset)
