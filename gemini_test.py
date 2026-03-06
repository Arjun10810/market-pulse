import os
from dotenv import load_dotenv
from google import genai
from tracker import get_crypto_price, get_stock_price

load_dotenv()

client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))

price = get_crypto_price("bitcoin")
contents = f"Bitcoin is currently at ${price}. What do you think about it?"

response = client.models.generate_content(
        model="gemini-2.5-flash", contents = contents

)
print(response.text)
