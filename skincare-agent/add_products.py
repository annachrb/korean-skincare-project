import pandas as pd

new_products = [
    {"product_name": "Madagascar Centella Ampoule", "product_brand": "Skin1004", "price": "€16", "product_description": "A lightweight ampoule with 100% Centella Asiatica extract that calms irritated and acne-prone skin, reduces redness, and strengthens the skin barrier. Ideal for sensitive and troubled skin.", "product_type": "Serum"},
    {"product_name": "Madagascar Centella Tone Brightening Capsule Ampoule", "product_brand": "Skin1004", "price": "€18", "product_description": "Brightening ampoule combining Centella Asiatica with Niacinamide to even out skin tone, fade dark spots, and reduce inflammation. Suitable for all skin types.", "product_type": "Serum"},
    {"product_name": "Madagascar Centella Hyalu-Cica Water-Fit Sun Serum SPF50+", "product_brand": "Skin1004", "price": "€19", "product_description": "Lightweight sunscreen serum with Centella and Hyaluronic Acid. Provides broad spectrum SPF50+ protection while hydrating and soothing sensitive skin. Non-greasy finish.", "product_type": "SPF/Sunscreen"},
    {"product_name": "Zimbabwe Wakati Brightening Capsule Cream", "product_brand": "Skin1004", "price": "€22", "product_description": "Brightening cream enriched with Baobab oil and Niacinamide to hydrate deeply, reduce hyperpigmentation, and restore radiance to dull skin.", "product_type": "Moisturizer"},
    {"product_name": "Heartleaf 77% Soothing Toner", "product_brand": "Anua", "price": "€22", "product_description": "A cult-favourite toner with 77% Heartleaf extract that deeply soothes irritated, acne-prone skin, minimizes pores, and controls excess sebum. Lightweight and fast-absorbing.", "product_type": "Toner"},
    {"product_name": "Heartleaf 70% Niacinamide Serum", "product_brand": "Anua", "price": "€26", "product_description": "Brightening serum combining Heartleaf extract with 10% Niacinamide to fade dark spots, even skin tone, and calm breakouts simultaneously.", "product_type": "Serum"},
    {"product_name": "Heartleaf Pore Control Cleansing Oil", "product_brand": "Anua", "price": "€24", "product_description": "Gentle cleansing oil with Heartleaf that dissolves makeup and sunscreen without stripping the skin. Suitable for sensitive and acne-prone skin.", "product_type": "Cleanser"},
    {"product_name": "Peach 70% Niacinamide Serum", "product_brand": "Anua", "price": "€26", "product_description": "Brightening serum with 70% peach extract and Niacinamide to improve skin texture, boost radiance, and reduce the appearance of pores.", "product_type": "Serum"},
    {"product_name": "Heartleaf Quercetinol Pore Deep Cleansing Foam", "product_brand": "Anua", "price": "€20", "product_description": "Low-pH cleansing foam that deeply cleans pores while maintaining the skin barrier. Contains Heartleaf and Quercetin to soothe and reduce inflammation.", "product_type": "Cleanser"},
    {"product_name": "Azelaic Acid 10 Hyaluron Redness Soothing Serum", "product_brand": "Anua", "price": "€29", "product_description": "A lightweight watery serum with 10% Azelaic Acid and 3 types of Hyaluronic Acid to calm redness, reduce acne, and fade post-blemish dark spots. Contains Anua's Gentle Calming Complex with Blue Tansy Oil, green tea leaf water, aloe, and 7 types of Cica to soothe irritation. Non-comedogenic, fragrance-free, and safe for sensitive skin. Can be used morning and night.", "product_type": "Serum"},
    {"product_name": "Green Tangerine Vita C Dark Spot Care Serum", "product_brand": "Goodal", "price": "€28", "product_description": "A brightening serum with 70% Jeju green tangerine extract, 4% Niacinamide, Arbutin, and stable Vitamin C. Visibly reduces dark spots and uneven skin tone in two weeks. Lightweight gel texture that absorbs quickly. Also contains Centella Asiatica for soothing sensitive skin. Suitable for all skin types.", "product_type": "Serum"},
    {"product_name": "Green Tangerine Vita C Moisture Cream", "product_brand": "Goodal", "price": "€24", "product_description": "Brightening and hydrating cream with Vitamin C and green tangerine to even skin tone and provide lasting moisture.", "product_type": "Moisturizer"},
    {"product_name": "Apricot Collagen Jelly Cream", "product_brand": "Goodal", "price": "€26", "product_description": "Bouncy jelly cream with Collagen and Apricot extract to firm skin, boost elasticity, and deeply hydrate for a plump appearance.", "product_type": "Moisturizer"},
    {"product_name": "Green Tangerine Vita C Toner Pad", "product_brand": "Goodal", "price": "€22", "product_description": "Exfoliating toner pads soaked in Vitamin C and AHA to brighten skin tone, smooth texture, and reduce dark spots with regular use.", "product_type": "Toner"},
    {"product_name": "Dokdo Toner", "product_brand": "Round Lab", "price": "€18", "product_description": "Hydrating toner with deep sea water and mineral extracts to balance skin, strengthen the barrier, and provide long-lasting moisture for all skin types.", "product_type": "Toner"},
    {"product_name": "Birch Juice Moisturizing Serum", "product_brand": "Round Lab", "price": "€22", "product_description": "Lightweight hydrating serum with 62% Birch Juice to deliver intense moisture, plump skin, and soothe dryness without heaviness.", "product_type": "Serum"},
    {"product_name": "1025 Dokdo Cream", "product_brand": "Round Lab", "price": "€22", "product_description": "Rich moisturizing cream with deep sea water and minerals to deeply nourish dry and sensitive skin while restoring the skin barrier.", "product_type": "Moisturizer"},
    {"product_name": "Birch Juice Moisturizing Cleanser", "product_brand": "Round Lab", "price": "€16", "product_description": "Gentle low-pH cleanser with Birch Juice that effectively removes impurities while keeping skin soft, hydrated, and balanced.", "product_type": "Cleanser"},
    {"product_name": "Birch Juice Moisturizing Sun Cream SPF50+ PA++++", "product_brand": "Round Lab", "price": "€19", "product_description": "A bestselling Korean sunscreen with Birch Sap, Niacinamide, and Hyaluronic Acid that provides SPF50+ PA++++ broad spectrum protection. Lightweight chemical sunscreen with no white cast, fragrance-free, and suitable for all skin types including sensitive and acne-prone. Voted best sunscreen on the Korean beauty app Hwahae.", "product_type": "SPF/Sunscreen"},
    {"product_name": "Birch Juice Moisturizing UV Lock Sunscreen SPF45", "product_brand": "Round Lab", "price": "€19", "product_description": "A hydrating chemical sunscreen with Birch Sap, Niacinamide, and Hyaluronic Acid. SPF45 broad spectrum, lightweight lotion texture with no white cast. Fragrance-free and gentle for sensitive and acne-prone skin. Doubles as a moisturizer for daily use.", "product_type": "SPF/Sunscreen"},
    {"product_name": "Birch Juice Mild-Up Mineral Sunscreen SPF50+ PA++++", "product_brand": "Round Lab", "price": "€21", "product_description": "A reef-safe mineral sunscreen with Birch Sap and Water Lily extract that reflects UV rays without skin absorption. SPF50+ PA++++ protection with a creamy texture that hydrates and soothes sensitive skin. Ideal for those with reactive or sensitive skin.", "product_type": "SPF/Sunscreen"},
    {"product_name": "Snail Mucin 96% Power Repairing Essence", "product_brand": "COSRX", "price": "€22", "product_description": "Iconic essence with 96% Snail Secretion Filtrate to repair the skin barrier, fade acne scars, deeply hydrate, and improve overall skin texture.", "product_type": "Serum"},
    {"product_name": "AHA 7 Whitehead Power Liquid", "product_brand": "COSRX", "price": "€24", "product_description": "Exfoliating liquid with 7% Glycolic Acid to dissolve dead skin cells, smooth texture, unclog pores, and brighten dull skin.", "product_type": "Toner"},
    {"product_name": "Some By Mi AHA BHA PHA 30 Days Miracle Toner", "product_brand": "Some By Mi", "price": "€18", "product_description": "Triple acid toner with AHA, BHA, and PHA that exfoliates, unclogs pores, and calms acne-prone skin over 30 days of consistent use.", "product_type": "Toner"},
    {"product_name": "Centella Asiatica 100 Ampoule", "product_brand": "Some By Mi", "price": "€20", "product_description": "Soothing ampoule with 100% Centella Asiatica to calm redness, repair damaged skin barrier, and reduce inflammation in sensitive skin.", "product_type": "Serum"},
    {"product_name": "Relief Sun Rice Probiotics SPF50+", "product_brand": "Beauty of Joseon", "price": "€18", "product_description": "Lightweight Korean sunscreen with Rice extract and Probiotics that protects against UV damage, brightens skin tone, and leaves a natural finish.", "product_type": "SPF/Sunscreen"},
    {"product_name": "Cicapair Tiger Grass Color Correcting Treatment SPF22", "product_brand": "Dr. Jart+", "price": "€38", "product_description": "Color-correcting cream that neutralizes redness, soothes irritation with Centella Asiatica, and provides light sun protection.", "product_type": "SPF/Sunscreen"},
    {"product_name": "Ceramidin Cream", "product_brand": "Dr. Jart+", "price": "€42", "product_description": "Rich barrier-repair cream with 5-Cera Complex to restore moisture, strengthen the skin barrier, and relieve dry and compromised skin.", "product_type": "Moisturizer"},
    {"product_name": "Vitamin C Boosting Serum", "product_brand": "Dr. Althea", "price": "€27", "product_description": "A brightening serum with 63% Hippophae Rhamnoides Water rich in Vitamin C, 5% Niacinamide, and 2% Tranexamic Acid to fade dark spots and even skin tone. Contains 8 types of Hyaluronic Acid for deep hydration and Centella Asiatica Leaf Water to soothe sensitive skin. Lightweight, non-sticky, vegan formula free from artificial colors and fragrance.", "product_type": "Serum"},
]

df_existing = pd.read_csv("enriched_products.csv", encoding="utf-8-sig")

last_id = df_existing["product_ID"].max()

new_rows = []
for i, product in enumerate(new_products):
    row = {
        "product_ID": last_id + i + 1,
        "product_name": product["product_name"],
        "product_brand": product["product_brand"],
        "price": product["price"],
        "product_description": product["product_description"],
        "product_type": product["product_type"],
        "skin_concerns": "",
        "skin_type": "",
        "key_ingredients": "",
        "when_to_use": ""
    }
    new_rows.append(row)

df_new = pd.DataFrame(new_rows)
df_combined = pd.concat([df_existing, df_new], ignore_index=True)
df_combined.to_csv("enriched_products.csv", index=False, encoding="utf-8-sig")
print(f"Added {len(new_rows)} products. Total: {len(df_combined)}")