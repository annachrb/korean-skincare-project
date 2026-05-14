# Glow Guide - Korean Skincare AI advisor
A conversational AI agent that recommends korean skincare products based on individual skin concerns, skin type and routine preferences.

## What it does
- Recommends Korean skincare products based on the user's skin concerns (acne, hyper pigmentation, dryness, sensitivity, aging)
- Suggests a night and morning routine based on the user's input
- Only recommends products from the dataset --> no hallucinated products
- Built with a RAG (Retrivial Augmented Generation) architecture

## How it works
1. A dataset of korean skincare products was enriched using a LLM to filter attributes (skin concerns, skin type, key ingredients, when to use)
2. The products are stored in a local vector database ChromDB and searched by semanting meaning
3. When the user asks for products, relevant ones are retrieved and passed to the LLM as context.
4. The LLM then generates a recommendation using only the retrieved products.
  
## Tech Stack

-  **Python**
-  **Groq AI** (LLaMA 3.3 70B) --> conversational AI
-  **ChromaDB** --> vector database for product search
-  **Streamlit** --> web interface
-  **Pandas** --> data processing

Product data sourced from [Soko Glam](https://sokoglam.com/) and enriched with additional popular korean skincare products from brands like Anua, Goodal, Round Lab, Skin1004, Beauty of Joseon.

## How to run locally

1. Clone repository
2. Install dependencies: pip install groq chromadb streamlit pandas python-dotenv
3. Add your Groq API key to a new ".env" file: GROQ_API_KEY=your_key_here
4. Load the product database: python load_data.py
5. Run the app: python -m streamlit run app.py

## Project context

As someone who has struggled with severe acne, I found it overwhelming to find skincare products that were actually effective vs just hype driven recommendations on Tiktok.
Glow Guide was built to cut through that noise. It recommends a routine based on individual concerns, with products that are actually popular in korea and that were effective for me personally.
This is no medical advice!
