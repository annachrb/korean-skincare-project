import pandas as pd
import re

def clean_text(x):
    if isinstance(x, str):
        x = x.replace("Â", "")
        x = re.sub(r'â€.', '', x)
        return x
    return x

df = pd.read_csv("enriched_products.csv", encoding="utf-8")
df = df.apply(lambda col: col.map(clean_text))
df.to_csv("enriched_products.csv", index=False, encoding="utf-8-sig")
print("Done! File cleaned.")