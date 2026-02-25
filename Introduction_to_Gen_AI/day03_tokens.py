# # TOKENS
# 
#  A token is the fundamental unit of text—such as a word, character, or subword—that AI models use to analyze and generate language. Through a process called tokenization, text is broken down into these smaller, manageable pieces, which are then converted into numerical representations (embeddings) for processing.
# 
#  https://platform.openai.com/tokenizer
# 
#  This website is what used by GPT model internally. You are preparing it the same way the model does before generating the output.

# -------

%pip install tiktoken

# tiktoken is a fast BPE tokeniser for use with OpenAI's models.
# Read more at https://github.com/openai/tiktoken

# Let's use this tiktoken to see how text is tokenized

# -------

import tiktoken

encoding = tiktoken.encoding_for_model("gpt-4o-mini")
tokens = encoding.encode("Hi, this is Mukilan and I am studying LLM from scratch")

# -------

tokens

# -------

for token_id in tokens:
  token_text = encoding.decode([token_id])
  print(f"{token_id} -> {token_text}")