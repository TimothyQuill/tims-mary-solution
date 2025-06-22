# 🚀 Software Engineer - ML Take‑Home Assessment

Welcome! This take-home task is designed to showcase your ability to build high-quality synthetic datasets for training large language models (LLMs).

---

## 1 · Problem Statement

Our users wade through thousands of OCR‑extracted legal documents and need low latency answers to ad‑hoc questions.

### Objective

Develop a script to generate synthetic training data for supervised fine-tuning (SFT) of an LLM. The goal is to teach the model to:

1. Handle queries about legal documents by generating one or more tool calls to retrieve information from:

   - Full-text stores (using BM25 ranking).
   - Vector stores (using cosine similarity on embeddings).

2. Focus exclusively on data generation—no need to implement:
   - Model training.
   - Answer generation logic.
   - Actual retrieval pipelines.

### Provided Data

- Two versions of a document are provided in the data folder:
  - The original document as a PDF (`data/document.pdf`)
  - A text version (`data/document_ocr.txt`) generated through OCR. The text file is organized with clear page demarcations (e.g., "==== PAGE 1 ===="). This represents the raw, unprocessed text before it gets indexed for searching
- Example user queries in `data/gold_queries.json`

### Deliverables

1. Python Script `main.py`

   - A Python script that generates the synthetic dataset. While we prioritize your methodological approach over implementation details, your code should still be well-structured and maintainable.

2. Output Dataset

   - A `dataset.jsonl` file containing at least 10 training examples.
   - Each row must follow this format:

   ```json
   {
     "query": "Find precedent cases about copyright infringement in the EU.",
     "tools": [
       {
         "name": "full_text_search",
         "arguments": { "query": "copyright infringement EU cases" }
       },
       ...
     ]
   }
   ```

   - The row may include additional custom fields as needed, but must always contain the `query` and `tools` fields.

3. Documentation

   - A `solution.md` file explaining:
     - Your approach to generating synthetic data.
     - Key design decisions and assumptions.
     - A diagram illustrating your data generation pipeline.
     - Any instructions required to run your script.

---

## 2 · Constraints & Tips

- Think outside the box. This task is purposefully open-ended, we care more about your thinking than actual code implementation.
- Must complete assessment within 1 week of receiving it.
- Create documentation explaining your design decisions.
- Be candid with what parts you used AI tools such as coding agents and ChatGPT to implement.
- The PDF of the OCR payload has been provided in the same `/data` folder, use it if needed.
- State any assumptions you have made

### Bonus points

- Reference a recently published paper that inspired your methodology or thinking. If you do this, make sure to reference it in the `solution.md`.

---

## 3. How to get started

1. Click `Use this repository` to create a `private` repo.
2. Clone your created repo and complete the task.

## 4 · Submission

1. Push code to a **private GitHub repo**.
2. Share access with `loz-maryapp` & `aaldulimi` **before the deadline**.
3. We will run your supplied instructions in `solution.md` and then organise a follow up interview.

---

## 5 · Follow‑Up Interview (90 min)

1. 5 min · Walkthrough of pipeline & design decisions.
2. 30 min · Deep‑dive Q&A on the synthetic‑data pipeline.
3. 45 min · Whiteboard Task.
4. 10 min · Your questions.

---

## 6 · FAQ

- **What about the API costs incurred during this take home?** We will happily reimburse you for the API credits used within reason!
- **What is the expected time commitment?** We recommend spending 2-4 hours on this assessment. Please try to stay within this timeframe.
- **What if I can't complete everything within the time limit?** Please document your approach and outline any planned next steps in your `solution.md` file.
- **Questions?** Email `laurence@marytechnology.com`.

Good luck & have fun! 🎉
