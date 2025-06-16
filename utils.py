import json
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def load_data():
    with open("business_data.json", "r") as f:
        return json.load(f)

def embed_texts(texts):
    return model.encode(texts)

def search_similar(query, data, top_k=3):
    docs = [f"{d['name']} - {d['description']} - {d['location']}" for d in data]
    doc_embeddings = embed_texts(docs)
    query_embedding = embed_texts([query])
    similarities = cosine_similarity(query_embedding, doc_embeddings)[0]
    top_indices = np.argsort(similarities)[-top_k:][::-1]
    return [data[i] for i in top_indices]
