from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
from dotenv import load_dotenv

load_dotenv()
client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-pro", contents="Explain huffman coding in Data compression"
)
print(response.text)