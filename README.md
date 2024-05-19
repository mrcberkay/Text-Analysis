Hello! 
This project is a product of a research unit at the University of Antwerp, as well as some brilliant external minds.
Essentially, this small, Embedding Model-based software helps you carry out textual cross-checking tasks with ease.\
The Embedding Model we used in this software is called: text-embedding-ada-002\
On this website, you can find more information: https://openai.com/blog/new-and-improved-embedding-model\
This project is useful, for instance, in comparing two texts and quickly identifying the similarities between them. We used this tool to check whether the students who used ChatGPT plagiarized in their essays, and it was very helpful!\
Please keep in mind that you will need an OpenAI API Key to use this software and you will be charged per inquiry!\
Here is everything explained in detail:\
First, you need any software that can run Python files and must have Python installed on your computer.\
Second, in the file "similarityUtils.py" you will find a line where you can enter your OpenAI API Key. Put your API key there.\
Third, you need to install certain packages. Below is a list of the packages (with their versions) that are necessary for this software to work. Use this command to install each package (replace X with the package name): pip install X\
annotated-types   0.6.0\
anyio             4.2.0\
certifi           2023.11.17\
colorama          0.4.6\
CTkListbox        1.2\
customtkinter     5.2.2\
darkdetect        0.8.0\
distro            1.9.0\
exceptiongroup    1.2.0\
h11               0.14.0\
httpcore          1.0.2\
httpx             0.26.0\
idna              3.6\
joblib            1.3.2\
numpy             1.26.3\
openai            1.8.0\
packaging         23.2\
pip               20.2.3\
pydantic          2.5.3\
pydantic-core     2.14.6\
pyperclip         1.8.2\
scikit-learn      1.3.2\
scipy             1.11.4\
setuptools        49.2.1\
sniffio           1.3.0\
threadpoolctl     3.2.0\
tqdm              4.66.1\
typing-extensions 4.9.0\
Fourth, once all the packages are installed, just click on "Run Python File" while you are on "main.py" and the software UI will pop up.\
You can add as many sentences as you want to the first text box. After you put in one sentence, click on "Add". However, if it is one long paragraph, check "If u enable it, gets and splits sentences too" before you add the paragraph.\
You can select and then remove sentences using the button "Remove Sentences".\
If you click on "Remove All" it will delete everything on the screen.\
The software will automatically separate the sentences in a paragraph when you put it in the second text box. You don't need to click on "Add" for the second text box, just put in the text.\
Hit "Confirm" once you put in everything you want to compare. It will produce results that are shown on the empty area.\
Clicking on "Copy All" will copy all the results on the screen.\
It may not be perfect, but this is as polished as we could manage for the time being. Feel free to use it in your projects!\
