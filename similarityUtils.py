import os
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from openai import OpenAI

os.environ["OPENAI_API_KEY"] = ""
client = OpenAI()


def get_embedding(texts, model="text-embedding-ada-002"):
    for t in texts:
        t = t.replace("\n", " ")

    embedding = client.embeddings.create(input=texts, model=model)
    return embedding


def get_similarities(sentences1, sentences2,threshold):
    sentence1_embeddings = get_embedding(sentences1)
    sentence2_embeddings = get_embedding(sentences2)

    sentence1_embeddings_reshaped = []
    sentence2_embeddings_reshaped = []

    for embedding in sentence1_embeddings.data:
        reshaped = np.array(embedding.embedding).reshape(1, -1)
        sentence1_embeddings_reshaped.append(reshaped)
    for embedding in sentence2_embeddings.data:
        reshaped = np.array(embedding.embedding).reshape(1, -1)
        sentence2_embeddings_reshaped.append(reshaped)

    similiarities = []

    for i in range(len(sentences1)):
        s1e = sentence1_embeddings_reshaped[i]
        currentSimiliarity = 0
        currentSimiliarityText = ""

        for j in range(len(sentences2)):
            s2e = sentence2_embeddings_reshaped[j]
            similiarity = cosine_similarity(s1e, s2e)[0][0]
            if(similiarity >= currentSimiliarity):
                currentSimiliarity = similiarity;
                s1text = str(sentences1[i])
                s2text = str(sentences2[j])
                currentSimiliarityText = f"{s1text} \t is copied from \t {s2text} \t with probablity of \t {str(round(similiarity,2))}"

        if(currentSimiliarity >= threshold):
            similiarities.append(currentSimiliarityText)

    return similiarities