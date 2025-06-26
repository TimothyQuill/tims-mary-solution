"""
Used ChatGPT to help refine these prompts...
"""

prompts = {
    "generate-query":
        """
            Instruction:
            Given the following legal document, generate 10 unique and content-specific questions that a user might ask after reading it.
            
            Guidelines:
            - All questions must be directly grounded in the **actual content** of the document.
            - Avoid generic legal questions. Do not use templates or boilerplate phrasing.
            - Ensure **diversity** across the questions:
              - Vary the legal focus (e.g. obligations, rights, penalties, definitions, timelines, exceptions)
              - Vary the scope (some narrow, some broad)
              - Vary the length and linguistic structure
            - Each question should reflect a **genuine information need** a user might have.
            
            Format:
            - Wrap each question in the tags `<<Q>>` and `<</Q>>`
            - Do **not** include numbering, headers, or any other text outside the tags
            
            Input:
            {0}
            
            Output:
            <<Q>>Question 1 text here<</Q>>
            <<Q>>Question 2 text here<</Q>>
            ...
            <<Q>>Question 10 text here<</Q>>
        """,

    "generate-label":
        """
            You are an expert in legal information retrieval.

            Given the user query:
            "{0}"
            
            And the following legal document:
            "{1}"
            
            Your task is to:
            
            1. Reflect step by step on which retrieval method is most suitable and why.
            2. Choose one of the following methods:
                - "full_text_search" — traditional keyword-based search (e.g., BM25)
                - "vector_search" — semantic embedding-based search
                - "hybrid_search" — a combination of both
            3. Suggest the most effective query to run using the selected method.
            
            Respond in the following format:
            
            Chain of thought reasoning here
            
            <<S>>search_method<</S>>
            <<Q>>recommended_query<</Q>>
        """
}
