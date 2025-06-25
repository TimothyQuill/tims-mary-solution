

Before I start coding, there's a few unique challenges that need to be considered.

1. The given legal document is very large (far too large for most prompt windows),
    so I need to define a way to ingest it so that enough context is provided for
    the model to ask effective questions.

2. I need to ensure that there is significant diversity in the queries.
   * A balance of classes being represented
   * A combination of long and short questions
   * A variation short and wide focus across scope of the document

3. I also need to consider to do I validate the accuracy of labels provided by the model.
    Discounting the option of hand-labelling the data, I am giving up some faith
    to the model. After all, if there were any heuristics we could use to validate the results, 
    then it would defeat the need for training a model. 
    
    Furthermore, ideally I would have the BM25 and vector store pipelines installed, 
    so that I could compare the top-k results produced by both search methods.
    This could act as a sort of ground-truth. Without it, the LLM has to rely on its 
    best estimation of how the search methods would perform.

4. Whilst the question/label structure of the data needs to be maintained, it's worth 
    considering how I can add additional custom fields I can add in order to 
    maximise the amount of information for the model to learn on.

I've made a few assumptions about the data, which in a professional capacity would need to be cleared up.

1. The goal of the data is to generalise to unseen documents, not the ones they're trained on.
2. The documents are open-source, and don't require any omissions, changes or redactions.
3. The data is for model distillation, not self-learning.
4. All provided legal documents will be complete and intact. 
5. The OCR generated will be of high quality with no errors.

My methodology

# Handling large files.
    
    When preparing my solution, I considered the following options:

   1. Use a model with a large context window (e.g. GPT-4.1-mini has a 1M token context window).
    While this solves the problem, is does feel a tiny bit like cheating, as our model should be
    robust enough to handle unseen documents, some of which will likely be above 1M tokens.

   2. Chunking the text. This option is simple and easy to implement. However, it potentially
    comes at the cost of a loss of context. Queries whose answer span a large portion of the 
    document will not perform well.

   3. Summarise sections. First chunk the text, and then for each chunk get the LLM to summarise 
    it. Then concatenating it together, and passing the summarised version to the LLM.
    The issue with this method is that it introduces additional noise to the text, increasing the
    likelihood of hallucinations occurring. 

   4. RAG system. This method would introduce the exact problem we're trying to solve, so screw that.

    Ultimately I decided the go with Gemini 2.5 Flash and introduce a chunking method that is activated
    when the input text is too large. Whilst it's not super ideal, it seems to be the best of the
    given options.
    
# Quality of queries
I tried to enforce quality in the queries by clearly outlining a set of guidelines for the model in the prompt.
I also tried to enforce diversity through the following methods:
* The temperature was turned up quite high, to promote a higher range of tokens. 
    This meant the model was less likely to repeat itself and explore a wider variety of possibilities.
* Top_p was set to .9, so that only a few tokens would get a chance to be selected. 
    This means that although the high temperature promotes diversity in the output,
    it wont go as far as allowing bad choices to be selected, and will reduce hallucinations.
* Finally, I got all of the queries to be selected at once, i.e. in a single API call.
    The logic for this is that a model is more likely to consider what has already been asked
    if they just generated the output.

# Quality of labels
To ensure the best quality of the labels, I did the following:
* Reduced the temperature to 0, so that it minimised the likelihood of any noise in the output.
* Promoted chain-of-thought reasoning, so that the model could analyse its decisions.

# Additional fields
I chose to include the chain-of-thought from each label generation to assist with finetuning
the model. The greater the context, the better it will be for the model to learn what actions to
take.

## Extensions

1. Lots of exception catches, and unit tests to ensure quality and consistency.

2. As I mentioned, implementing the search pipelines, and using the output as a source of ground-truth
    would be a good way to ensure the accuracy of the labels.

3. Another option to increase accuracy would be to create a committee of LLMs (ChatGPT, Gemini, Claude, etc).
    Each model will be asked to label the output, and a poll would be conducted. If there is not a uniform
    response, each model will be shown each other model's chain-of-thought, and then asked to reassess.
    This process could go round until there is a consensus or a majority. In practical terms, this is 
    possibly overkill, but is worth considering.

4. +