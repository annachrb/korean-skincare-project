import pandas as pd
from groq import Groq
from dotenv import load_dotenv
import os
import time

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

df = pd.read_csv("enriched_products.csv", encoding="utf-8-sig", dtype={"skin_concerns": str, "skin_type": str, "key_ingredients": str, "when_to_use": str})
def enrich_product(description, product_type):
    prompt = f"""
You are a skincare expert. Based on this product description and type, extract the following information.
Respond ONLY in this exact format, nothing else:

SKIN_CONCERNS: [comma separated, e.g. acne, aging, dryness, hyperpigmentation, sensitivity, oiliness, dullness]
SKIN_TYPE: [comma separated, e.g. oily, dry, combination, sensitive, all]
KEY_INGREDIENTS: [comma separated, max 3]
WHEN_TO_USE: [morning, night, or both]

Product type: {product_type}
Description: {description}
"""
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(10)
        return None

def parse_response(text):
    result = {
        "skin_concerns": "",
        "skin_type": "",
        "key_ingredients": "",
        "when_to_use": ""
    }
    if not text:
        return result
    for line in text.splitlines():
        if line.startswith("SKIN_CONCERNS:"):
            result["skin_concerns"] = line.replace("SKIN_CONCERNS:", "").strip()
        elif line.startswith("SKIN_TYPE:"):
            result["skin_type"] = line.replace("SKIN_TYPE:", "").strip()
        elif line.startswith("KEY_INGREDIENTS:"):
            result["key_ingredients"] = line.replace("KEY_INGREDIENTS:", "").strip()
        elif line.startswith("WHEN_TO_USE:"):
            result["when_to_use"] = line.replace("WHEN_TO_USE:", "").strip()
    return result

skipped = 0
processed = 0

for i, row in df.iterrows():
    if pd.notna(row["skin_concerns"]) and str(row["skin_concerns"]).strip() != "":
        skipped += 1
        continue

    print(f"Processing {i+1}/{len(df)}: {row['product_name']}")
    raw = enrich_product(str(row["product_description"]), str(row["product_type"]))
    parsed = parse_response(raw)

    df.at[i, "skin_concerns"] = parsed["skin_concerns"]
    df.at[i, "skin_type"] = parsed["skin_type"]
    df.at[i, "key_ingredients"] = parsed["key_ingredients"]
    df.at[i, "when_to_use"] = parsed["when_to_use"]
    processed += 1
    time.sleep(2)

df.to_csv("enriched_products.csv", index=False, encoding="utf-8-sig")
print(f"Done! Processed {processed} new products, skipped {skipped} already enriched.")