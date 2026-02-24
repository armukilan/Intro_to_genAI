%pip install google-genai python-dotenv

# -------

from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='../.env')

API_KEY = os.environ["GOOGLE_API_KEY"]

client = genai.Client(api_key=API_KEY)
response = client.models.generate_content(
    model = 'gemini-2.5-flash',
    contents="Hii, this is Mukilan, Masters student in Computer Science, experienced in Python, Machine Learning, Deep Learning and learning Gen AI concepts. Write a short notes about me."
)

print(response.text)