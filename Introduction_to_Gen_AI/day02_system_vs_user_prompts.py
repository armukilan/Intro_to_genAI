# # What is a User prompt?
# 
# A user prompt is the direct instruction or question that you send to the AI model. That's what the user asks for.
# 
# # What is a System Prompt?
# 
# A system prompt (system instruction) is a hidden instruction that sets the behaviour, tone and the role of AI. It shapes how the Ai responds to user prompts.

# -------

# User prompt without system prompt

from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='../.env')
API_KEY = os.environ["GOOGLE_API_KEY"]
client = genai.Client(api_key=API_KEY)

user_prompt = "Describe Garlic Cheesy bread in one sentence"

response = client.models.generate_content(
    model = "gemini-2.5-flash-lite",
    contents = user_prompt
)

print("Without system prompt")
print(response.text)

# -------

# User prompt with system prompt

from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

# load_dotenv(dotenv_path='../.env')
# API_KEY = os.environ["GOOGLE_API_KEY"]
# client = genai.Client(api_key=API_KEY)

user_prompt = "Describe Garlic Cheesy bread in one sentence"
system_prompt = "You are a 5-star chef running a Michelin star restaurent"

response = client.models.generate_content(
    model = "gemini-2.5-flash-lite",
    contents = user_prompt,
    config = types.GenerateContentConfig(systemInstruction= system_prompt)
)

print("With system prompt")
print(response.text)