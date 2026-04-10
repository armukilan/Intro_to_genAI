# 🤖 GenAI Learning Journey

Generative AI (GenAI) is a branch of artificial intelligence focused on building models that can generate new content — such as text, images, code, and more — based on patterns learned from data. It powers tools like ChatGPT, image generators, and code assistants that have taken the world by storm.

My goal is simple: **learn Generative AI from the ground up**. I'm taking it step by step, building my understanding through hands-on practice and experimentation. This repository serves as my personal learning log — it contains all the Python code I write along the way, organized as I progress through concepts and projects.

## 🛠️ Setup & Workflow

I run all my code on **Google Colab**, with my Google Drive and GitHub directly integrated — so I can version control my work without leaving Colab.

### 🔗 Linking Google Colab with GitHub

The first step is to setup a Github Personal Access token.

### 🔑 Setting Up a GitHub Personal Access Token

Since Colab doesn't store credentials, you need a **GitHub Personal Access Token (PAT)** to authenticate and push code.

**Steps to generate your token:**
1. Go to GitHub → **Settings** → **Developer Settings** → **Personal Access Tokens** → **Tokens (classic)**
2. Click **Generate new token**
3. Give it a name, set expiry, and check the **`repo`** scope
4. Copy the token — you won't see it again!


Next, you can use the below code to authenticate your colab with your Github account.
```python

import os
from google.colab import userdata

# GitHub setup
GITHUB_TOKEN = userdata.get("GITHUB_TOKEN")
REPO = "REPO_NAME"
USERNAME = "user_name"
TARGET_FOLDER = "target_folder" #IF any

# Clone repo
!git clone https://{GITHUB_TOKEN}@github.com/{USERNAME}/{REPO}.git
!git config --global user.email "user_email"
!git config --global user.name "user_mail."

!git -C /content/{REPO} remote set-url origin https://{GITHUB_TOKEN}@github.com/{USERNAME}/{REPO}.git
```


After all your code is done, you have to mount drive

```python
# Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')
```
After doing this, work with the saved copy, not with the original one.



Next is pushing your code from Google Colab to Github.
When you run your code, you'll run it in different cells.
Use this comment in each cell, that you feel shouldn't be pushed to your Github repo

```python
# ============================================================
# PUSH CELL1 — Do not push this cell
# ============================================================

# ============================================================
# PUSH CELL2 — Do not push this cell
# ============================================================

# ============================================================
# PUSH CELL3 — Do not push this cell
# ============================================================
```
Basically what this does is, it says which cells should't be pushed.
In the next step, we'll mention it, and those will not be pushed

### 📄 Converting .ipynb to .py and Pushing to GitHub
```python
import nbformat, re
from google.colab import drive

REPO = "repo_name
TARGET_FOLDER = "folder_name"
FILE_NAME = "something.py"  # Change this each day

# Get the current notebook
NOTEBOOK_PATH = "/content/drive/MyDrive/Colab Notebooks/notebook.ipynb"

# Read notebook and extract only real code cells
# Skips any cell containing the markers below
SKIP_MARKERS = ["PUSH CELL1", "PUSH CELL2", "PUSH CELL3"]

with open(NOTEBOOK_PATH, "r") as f:
    nb = nbformat.read(f, as_version=4)

code_lines = []
for cell in nb.cells:
    if cell.cell_type == "code":
        source = cell.source
        if any(marker in source for marker in SKIP_MARKERS):
            continue  # Skip setup and push cells
        if source.strip():
            code_lines.append(source)

    elif cell.cell_type == "markdown":
        lines = cell.source.strip().split("\n")
        commented = "\n".join(f"# {line}" for line in lines)
        code_lines.append(commented)

# Write clean .py file
output_path = f"/content/{FILE_NAME}"
with open(output_path, "w") as f:
    f.write("\n\n# -------\n\n".join(code_lines))

print(f"✅ Clean code written to {FILE_NAME}")
print("Preview:\n")
print(open(output_path).read()[:500])

# Push to GitHub
dest = f"/content/{REPO}/{TARGET_FOLDER}/{FILE_NAME}"
!cp {output_path} /content/{REPO}/{TARGET_FOLDER}/
%cd /content/{REPO}
!git add {TARGET_FOLDER}/{FILE_NAME}
!git commit -m "Add {FILE_NAME}"
!git push
print("✅ Pushed to GitHub successfully!")
```

> **Note:** Only the clean, relevant `.py` files are pushed to this repo — not the raw notebooks — to keep things organized and readable.


### Preserving the original .ipynb format

Now, I have revised my files to save as `.ipynb` fomat. Use this one instead of the above one

```
# ============================================================
# PUSH CELL — Do not push this cell
# ============================================================
import nbformat
from google.colab import drive

REPO = "repo_name
TARGET_FOLDER = "folder_name"
FILE_NAME = "something.py"  # Change this each day

NOTEBOOK_PATH = "/content/drive/MyDrive/file_name.ipynb"  # Update this

SKIP_MARKERS = ["SETUP CELL", "MOUNT CELL", "PATH CELL", "PUSH CELL", "GITHUB CELL"]

# Read the original notebook
with open(NOTEBOOK_PATH, "r") as f:
    nb = nbformat.read(f, as_version=4)

# Filter out unwanted cells
filtered_cells = []
for cell in nb.cells:
    source = cell.source
    if any(marker in source for marker in SKIP_MARKERS):
        continue  # Skip these cells entirely
    filtered_cells.append(cell)

# Build a clean notebook with only the filtered cells
clean_nb = nbformat.v4.new_notebook()
clean_nb.cells = filtered_cells
clean_nb.metadata = nb.metadata  # Preserve kernel/language metadata

# Write the clean notebook
output_path = f"/content/{FILE_NAME}"
with open(output_path, "w") as f:
    nbformat.write(clean_nb, f)

print(f"✅ Clean notebook written to {FILE_NAME}")
print(f"   Total cells kept: {len(filtered_cells)}")

# Push to GitHub
!cp {output_path} /content/{REPO}/{TARGET_FOLDER}/
%cd /content/{REPO}
!git add {TARGET_FOLDER}/{FILE_NAME}
!git commit -m "Add {FILE_NAME}"
!git push

print("✅ Pushed to GitHub successfully!")
```
> **Note:** Preserves the `.ipynb` structure - including the cells, formatting and the code.
