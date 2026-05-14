import pandas as pd
import chromadb
from chromadb.utils import embedding_functions
import os

df = pd.read_csv("enriched_products.csv")

client = chromadb.PersistentClient(path="./chroma_db")

try:
    client.delete_collection("skincare_products")
except:
    pass

collection = client.create_collection(
    name="skincare_products",
    embedding_function=embedding_functions.DefaultEmbeddingFunction()
)

documents = []
metadatas = []
ids = []

for i, row in df.iterrows():
    text = f"""
    Product: {row['product_name']}
    Brand: {row['product_brand']}
    Type: {row['product_type']}
    Skin Concerns: {row['skin_concerns']}
    Skin Type: {row['skin_type']}
    Key Ingredients: {row['key_ingredients']}
    When to use: {row['when_to_use']}
    Description: {str(row['product_description'])[:300]}
    """
    documents.append(text)
    metadatas.append({
        "product_name": str(row['product_name']),
        "product_brand": str(row['product_brand']),
        "price": str(row['price']),
        "product_type": str(row['product_type']),
        "skin_concerns": str(row['skin_concerns']),
        "skin_type": str(row['skin_type']),
        "key_ingredients": str(row['key_ingredients']),
        "when_to_use": str(row['when_to_use'])
    })
    ids.append(str(i))

collection.add(documents=documents, metadatas=metadatas, ids=ids)
print(f"Loaded {len(documents)} products into ChromaDB")