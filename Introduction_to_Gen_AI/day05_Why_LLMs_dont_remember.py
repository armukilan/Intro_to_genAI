# # LLM dont remember.
# 
#  - LLM's don't remember anything. They appear to remember stuff.
#  - Every API call is stateless, so the model only know what you send in that particular request.
# 
# Let's see an example

# -------

# So, in this example, let's introduce ourself.
from google import genai
from google.genai import types
import os

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Hey, My name is Mukilan"
)

print(response.text)

# -------

# Now, let's ask a follow up question

response2 = client.models.generate_content(
    model = "gemini-2.5-flash-lite",
    contents = "What is my name?"
)

print(response2.text)

# -------

# So, what do developers do?

# -------

messages = [
    types.Content(
        role = "user",
        parts = [types.Part(text="Hii, this is Mukilan")]
    ),

    types.Content(
        role = "model",
        parts = [types.Part(text="Hii Mukilan, how can I assist you today?")]
    ),

    types.Content(
        role = "user",
        parts = [types.Part(text="What's my name?")]
    ),
]

response3 = client.models.generate_content(
    model = "gemini-2.5-flash-lite",
    contents = messages
)

print(response3.text)

# -------

# Developers store the history of previous chat in list or in memory and simulate thet the AI can remember stuff.