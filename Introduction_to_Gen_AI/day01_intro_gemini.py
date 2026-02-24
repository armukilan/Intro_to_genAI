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

# -------

# Great, you're ready to push! Here's what to do next:
# First, make sure your notebook is saved in Google Drive. In Colab, go to File → Save a copy in Drive. This saves it to your Drive so the push cell can read it.
# Then mount Drive by running this cell:

from google.colab import drive
drive.mount('/content/drive')

# After doing this, work with the saved copy, not with the original one.

# -------

# Then find your notebook's exact path by running:
!find /content/drive/MyDrive -name "*Introduction*" 2>/dev/null