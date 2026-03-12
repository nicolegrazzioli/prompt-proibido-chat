import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import errors

load_dotenv()
api_key = os.environ.get("API_KEY")

if not api_key:
    print("API KEY NOT FOUND")
    sys.exit(1)

client = genai.Client(api_key=api_key)

models = [
    "gemini-1.5-flash",
    "gemini-1.5-flash-8b",
    "gemini-1.5-pro",
    "gemini-2.0-flash",
    "gemini-2.0-flash-lite-preview-02-05",
    "gemini-1.0-pro"
]

for m in models:
    print(f"\n--- Testando modelo: {m} ---")
    try:
        response = client.models.generate_content(model=m, contents="oi")
        print(f"SUCESSO! Resposta: {response.text[:20]}...")
    except errors.APIError as e:
        print(f"ERRO API: {e.code} - {e.message}")
    except Exception as e:
        print(f"ERRO: {e}")
