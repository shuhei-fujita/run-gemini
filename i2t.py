# Image to Text(I2T) のサンプルコード

# Gemini API では、使用するモデル バリエーションに応じて、テキストデータと画像データの両方をプロンプトに使用できます。
# たとえば、gemini-pro モデルではテキスト プロンプトを使用してテキストを生成し、gemini-pro-vision モデルではテキストデータと画像データの両方を使用します。
# https://ai.google.dev/docs/gemini_api_overview?hl=ja#generate_content

import google.generativeai as genai
import os
from dotenv import load_dotenv
from pathlib import Path
import PIL.Image

if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("API_KEY")
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-pro-vision")
    prompt_text = "Do these look store-bought or homemade?"
    prompt_image = PIL.Image.open("sample2.png")

    response = model.generate_content([prompt_text, prompt_image])
    print(response.text)
