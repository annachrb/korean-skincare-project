import streamlit as st
import chromadb
from chromadb.utils import embedding_functions
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_collection(
    name="skincare_products",
    embedding_function=embedding_functions.DefaultEmbeddingFunction()
)

st.set_page_config(
    page_title="Glow Guide",
    page_icon="🌿",
    layout="centered"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300&family=DM+Sans:wght@300;400&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    font-weight: 300;
}

.stApp {
    background-color: #faf8f5;
}

.main .block-container {
    padding-top: 2rem;
    max-width: 720px;
}

.hero {
    text-align: center;
    padding: 2.5rem 1rem 1.5rem 1rem;
}

.hero h1 {
    font-family: 'Cormorant Garamond', serif;
    font-size: 3.2rem;
    font-weight: 300;
    color: #2c2c2c;
    letter-spacing: 0.02em;
    margin-bottom: 0.3rem;
    line-height: 1.1;
}

.hero h1 em {
    font-style: italic;
    color: #a0856c;
}

.hero p {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.9rem;
    color: #999;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-top: 0.5rem;
}

.divider {
    width: 40px;
    height: 1px;
    background: #d4b89a;
    margin: 1rem auto 2rem auto;
}

.suggestion-row {
    display: flex;
    gap: 0.5rem;
    flex-wrap: wrap;
    justify-content: center;
    margin-bottom: 1.5rem;
}

.suggestion-pill {
    background: #f0ebe4;
    border: 1px solid #e0d5ca;
    border-radius: 20px;
    padding: 0.4rem 1rem;
    font-size: 0.78rem;
    color: #7a6a5e;
    cursor: pointer;
    letter-spacing: 0.03em;
    transition: all 0.2s;
}

.suggestion-pill:hover {
    background: #e8ddd4;
    color: #5a4a3e;
}

/* Chat messages */
.stChatMessage {
    background: transparent !important;
    border: none !important;
    padding: 0.5rem 0 !important;
}

[data-testid="stChatMessageContent"] {
    background: #ffffff !important;
    border: 1px solid #ede8e2 !important;
    border-radius: 16px !important;
    padding: 1rem 1.2rem !important;
    font-size: 0.92rem !important;
    line-height: 1.7 !important;
    color: #3a3a3a !important;
    box-shadow: 0 1px 4px rgba(0,0,0,0.04) !important;
}

[data-testid="stChatMessageContent"] p {
    color: #3a3a3a !important;
}

/* User message different color */
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) [data-testid="stChatMessageContent"] {
    background: #f5ede6 !important;
    border-color: #e8d8cc !important;
}

/* Input box */
[data-testid="stChatInput"] {
    border-radius: 30px !important;
    border: 1px solid #ddd6ce !important;
    background: #ffffff !important;
    font-size: 0.9rem !important;
}

[data-testid="stChatInput"]:focus {
    border-color: #c4a882 !important;
    box-shadow: 0 0 0 2px rgba(196,168,130,0.15) !important;
}

/* Hide streamlit branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>Glow <em>Guide</em></h1>
    <p>Korean Skincare · Personalised Recommendations</p>
    <div class="divider"></div>
</div>
""", unsafe_allow_html=True)

suggestions = [
    "🌿 Oily & acne-prone morning routine",
    "💧 Dry skin hydration boost",
    "✨ Brighten dark spots",
    "🌙 Anti-aging night routine",
    "🌸 Sensitive skin routine",
    "🫧 What cleanser for combination skin?",
]

cols = st.columns(3)
for i, s in enumerate(suggestions):
    if cols[i % 3].button(s, key=f"sug_{i}", use_container_width=True):
        st.session_state["prefill"] = s

st.markdown("<br>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prefill = st.session_state.pop("prefill", None)
prompt = st.chat_input("Tell me about your skin...") or prefill

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    last_messages = [m["content"] for m in st.session_state.messages[-3:]]
    search_query = " ".join(last_messages)
    results = collection.query(query_texts=[search_query], n_results=15)

    metadatas = results["metadatas"][0]
    brands_mentioned = [word for word in search_query.lower().split() if len(word) > 3]
    extra = collection.query(query_texts=[prompt], n_results=5, where=None)
    all_metadatas = metadatas + [m for m in extra["metadatas"][0] if m not in metadatas]
    
    
    product_context = ""
    for i, metadata in enumerate(all_metadatas):
        product_context += f"""
Product {i+1}:
- Name: {metadata['product_name']}
- Brand: {metadata['product_brand']}
- Price: {metadata['price']}
- Type: {metadata['product_type']}
- Best for concerns: {metadata['skin_concerns']}
- Skin type: {metadata['skin_type']}
- Key ingredients: {metadata['key_ingredients']}
- When to use: {metadata['when_to_use']}
"""

    system_prompt = f"""You are a knowledgeable and friendly Korean skincare advisor.

    STRICT RULES:
    - You ONLY recommend products from the AVAILABLE PRODUCTS list below. Never recommend any product not in this list.
    - If asked about a product you previously recommended, refer back to that exact product by name. Never switch products mid-conversation.
    - If asked for reviews, say you don't have review data but suggest checking Soko Glam, YesStyle, or Stylevana for reviews on the specific product you recommended.
    - Never say a product you just recommended "is not on the list" — if you recommended it, it is on the list.
    - Always mention product name, brand, and price.
    - Keep your tone warm, clear and concise.

    If the user mentions acne, prioritize products with niacinamide, salicylic acid, propolis, azelaic acid, or centella.
    If the user mentions aging, prioritize retinol, retinal, or peptides.
    If the user mentions dryness, prioritize hyaluronic acid or ceramides.
    If the user mentions brightening or dark spots, prioritize vitamin C, niacinamide, or arbutin.
    If the user asks for a morning routine, only recommend products where when_to_use is morning or both.
    If the user asks for a night routine, only recommend products where when_to_use is night or both.

    AVAILABLE PRODUCTS based on the user's query:
    {product_context}
    """

    messages_for_api = [{"role": "system", "content": system_prompt}]
    for msg in st.session_state.messages:
        messages_for_api.append({"role": msg["role"], "content": msg["content"]})

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages_for_api,
        temperature=0.5
    )

    answer = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)