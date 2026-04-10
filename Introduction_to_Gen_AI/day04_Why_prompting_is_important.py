# Normal prompt

from google import genai
from google.genai import types
import os

API_KEY = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=API_KEY)

user_prompt = "Hii, this is Mukilan, how are you?"

response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = user_prompt
)

print(response)

# -------

print(f"Response text: {response.text}")

print(f"Total token count: {response.usage_metadata.total_token_count}")
print(f"Input token count: {response.usage_metadata.prompt_token_count}")
print(f"Output token count: {response.usage_metadata.candidates_token_count}")
print(f"Thought token count: {response.usage_metadata.thoughts_token_count}")

# -------

# # Why tokens matter: The economics
# 
# Tokens are the currency of AI. Here's what you need to know:
# 
# 1. You pay per token (Input + Output)
#   
#     a. Every word you send costs money
#     
#     b. Every word AI generates cost money
# 
# 2. Different models have different pricing
# 
# 3. One word is not equal to one token.
# 
# 4. Context windows are limited.
# 
#     a. Every prompt you send uses up your available memory
#     
#     b. Long prompt = LEss space for conversation
# 
#     c. Less space: Worst context awareness = worse answers

# -------

# Bad Prompting

user_prompt = "Explain about Database in brief"

response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = user_prompt
)

print(f"Response text: {response.text}")

print(f"Total token count: {response.usage_metadata.total_token_count}")
print(f"Input token count: {response.usage_metadata.prompt_token_count}")
print(f"Output token count: {response.usage_metadata.candidates_token_count}")
print(f"Thought token count: {response.usage_metadata.thoughts_token_count}")

# -------

# Good Prompt

user_prompt = """You are a helpful assistant for college students. Your job is to explain technical concepts in simple language. Use example wherever posiible.
Avoid jargon and technical terms, be friendly and encouraging. Keep responses concise but complete.
Now, explain what is a database to a college student, with a real life example, explain why databses are important and keep it under five sentences"""

response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = user_prompt
)

print(f"Response text: {response.text}")

print(f"Total token count: {response.usage_metadata.total_token_count}")
print(f"Input token count: {response.usage_metadata.prompt_token_count}")
print(f"Output token count: {response.usage_metadata.candidates_token_count}")
print(f"Thought token count: {response.usage_metadata.thoughts_token_count}")