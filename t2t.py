# Text to Text Transfer Transformer (T2T) のサンプルコードです

import google.generativeai as genai
import os
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("API_KEY")
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(
        "What is the meaning of life? Response is 160 characters."
    )
    print(response.text)
