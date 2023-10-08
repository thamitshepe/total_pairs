from fastapi import FastAPI, Query
from typing import List

import re

app = FastAPI()

def calculate_total_pairs(texts):
    total_pairs = 0

    for text in texts:
        # Use regular expressions to extract the size and quantity
        match = re.search(r'(\d+(?:\.\d+)?)(?:[a-zA-Z]?[xX-]\s*(\d+))?', text)

        if match:
            quantity = int(match.group(2)) if match.group(2) is not None else 1
            total_pairs += quantity

            if match.group(1) == '' and match.group(2) is None:
                total_pairs += 1  # Add 1 if there's no quantity and the size is alone

    return total_pairs

@app.post("/calculate")
async def calculate(texts: List[str] = Query(..., description="List of texts separated by line breaks or commas")):
    result = calculate_total_pairs(texts)
    return {"total_pairs": result}
