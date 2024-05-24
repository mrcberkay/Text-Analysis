# Hello!

This project is a product of a research unit at the University of Antwerp, as well as some brilliant external minds.

Essentially, this small, Embedding Model-based software helps you carry out textual cross-checking tasks with ease.

## The Embedding Model

The Embedding Model we used in this software is called: text-embedding-ada-002.
You can find more information on the OpenAI website: https://openai.com/blog/new-and-improved-embedding-model

## Why Use This Project?

This project is useful, for instance, in comparing two texts and quickly identifying the similarities between them. We used this tool to check whether the students who used ChatGPT plagiarized in their essays, and it was very helpful!

**Please keep in mind that you will need an OpenAI API Key to use this software, and you will be charged per inquiry!**

## Setup Instructions

1. **Install Python:** Ensure you have Python 3.9.0 installed on your computer. Also make sure to tick "Add Python 3.9.0 to PATH" during the installation process.
2. **Get an OpenAI API Key:** Visit the OpenAI website to obtain your API key. Make sure that your account has enough credit.
3. **Install VS Code or similar:** This software will work with Visual Studio Code, but you can use another app that can run Python files.
4. **Extract the ZIP:** After downloading the ZIP file from Github (Code > Download ZIP), extract it to a folder that you created specifically for these files.
5. **Edit `similarityUtils.py`:**
    * Open the file `similarityUtils.py` in a text editor (VS Code, PyCharm, etc.).
    * Locate the line for the API key (line 6) and put your key between the quotation marks. 

6. **Install Packages:** These packages are required for text processing, UI elements, and interacting with the OpenAI API. Install each using the following command (replace `X` with the package name):
   ```bash
   pip install X
   
* annotated-types   0.6.0
* anyio             4.2.0
* certifi           2023.11.17
* colorama          0.4.6
* CTkListbox        1.2
* customtkinter     5.2.2
* darkdetect        0.8.0
* distro            1.9.0
* exceptiongroup    1.2.0
* h11               0.14.0
* httpcore          1.0.2
* httpx            0.26.0
* idna              3.6
* joblib            1.3.2
* numpy             1.26.3
* openai            1.8.0
* packaging         23.2
* pip               20.2.3
* pydantic          2.5.3
* pydantic-core     2.14.6
* pyperclip         1.8.2
* scikit-learn      1.3.2
* scipy             1.11.4
* setuptools        49.2.1
* sniffio           1.3.0
* threadpoolctl     3.2.0
* tqdm              4.66.1
* typing-extensions 4.9.0


7. **Run the Software:** Start Visual Studio Code (downloaded seperately from Microsoft's website). Go to "File" then "Open Folder" and select the folder where you extracted the files. Open main.py and click "Run Python File." The software UI will appear.

**Using the Software**  
**First Text Box:** Add sentences one by one (click "Add") or paste a whole paragraph (check the "If u enable it, gets and splits sentences too" box).  
**Second Text Box:** Paste the text you want to compare. The software will automatically split sentences.  
**Remove Sentences:** Select sentences in the list and click "Remove Sentences."  
**Remove All:** Clears all text.  
**Confirm:** Click "Confirm" to start the comparison.  
**Copy All:** Copies the results to your clipboard.  
  
If you are interested in improving this tool or have questions, feel free to reach out! You can also make changes for your personal use.
