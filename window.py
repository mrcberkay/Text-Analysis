import pyperclip as pc
import tkinter as tk
from tkinter import ttk
import re
import customtkinter
from CTkListbox import *
import similarityUtils

sentenceCount = 0

root = customtkinter.CTk()
root.geometry("720x920")
root.title("Tofu")

customtkinter.set_appearance_mode("Dark")

selectedOption = ""
sentence_pattern = r'(?<=[.!?])\s+'

def selectEntrySentence(selected):
    global selectedOption
    selectedOption = selected


def checkBoxChanged():
    print()




def insertSentence():
    global sentenceCount
    sentenceListbox.insert(sentenceCount, str(sentenceEntry.get().strip()))
    sentenceCount = sentenceCount + 1
    sentenceEntry.delete(0, tk.END)


def removeSelected():
    sentenceListbox.delete("all")


def selectEntryResult(selected):
    pc.copy(selected)


def Process():
    resultListbox.delete("all")

    sentences = []
    if (checkBox.get() == "on"):
        for sentence in sentenceListbox.get("all"):
            splitted = re.split(sentence_pattern, sentence)
            for s in splitted:
                sentences.append(str(s))
    else:
        sentences = sentenceListbox.get("all")

    paragraph = paragraphEntry.get().strip()
    paragraph = re.split(sentence_pattern, paragraph)
    paragraphs = []
    for p in paragraph:
        paragraphs.append(str(p))

    for s in sentences:
        s = s.strip()
    for p in paragraphs:
        p = p.strip()


    similarities = similarityUtils.get_similarities(sentences,paragraphs,scoreThreshold)
    for s in similarities:
        resultListbox.insert(resultListbox.size(), s)






def copyAll():
    copy = ""
    for res in resultListbox.get("all"):
        copy += f"{res} \n"
    pc.copy(copy)


def removeAll():
    resultListbox.delete("all")
    sentenceListbox.delete("all")
    sentenceEntry.delete(0, tk.END)
    paragraphEntry.delete(0, tk.END)


checkBox = tk.StringVar()
sentenceListbox = CTkListbox(root, command=selectEntrySentence)

sentenceEntry = customtkinter.CTkEntry(master=root,
                                           width=720,
                                           height=25,
                                           corner_radius=10)

paragraphEntry = customtkinter.CTkEntry(master=root,
                                            width=720,
                                            height=25,
                                            corner_radius=10)
resultListbox = CTkListbox(root, command=selectEntryResult)

def drawWindow(threshold):
    global scoreThreshold
    scoreThreshold = threshold

    sentenceListbox.pack(fill="both", expand=True, padx=10, pady=10)

    sentenceEntry.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
    sentenceEntry.pack(pady=20)



    ttk.Checkbutton(root,
                    text='If u enable it, gets and splits sentences too.',
                    command=checkBoxChanged,
                    variable=checkBox,
                    onvalue='on',
                    offvalue='off').pack()

    addSentenceButton = customtkinter.CTkButton(
        root,
        text='Add Sentence',
        fg_color='#FF0',
        text_color='#000',
        hover_color='#AA0',
        command=lambda: insertSentence())
    addSentenceButton.pack()

    removeSelectedButton = customtkinter.CTkButton(
        root,
        text='Remove Sentences',
        fg_color='#FF0',
        text_color='#000',
        hover_color='#AA0',
        command=lambda: removeSelected())
    removeSelectedButton.pack()

    paragraphEntry.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
    paragraphEntry.pack(pady=20)

    confirmButton = customtkinter.CTkButton(
        root,
        text='Confirm',
        fg_color='#FF0',
        text_color='#000',
        hover_color='#AA0',
        command=lambda: Process())
    confirmButton.pack()

    copyAllButton = customtkinter.CTkButton(
        root,
        text='Copy All',
        fg_color='#FF0',
        text_color='#000',
        hover_color='#AA0',
        command=lambda: copyAll())
    copyAllButton.pack()

    resultListbox.pack(fill="both", expand=True, padx=10, pady=10)

    removeAllButton = customtkinter.CTkButton(
        root,
        text='Remove All',
        fg_color='#FF0',
        text_color='#000',
        hover_color='#AA0',
        command=lambda: removeAll())
    removeAllButton.pack()

    root.mainloop()

