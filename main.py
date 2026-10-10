import os
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env
load_dotenv()

# Read the API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

# Create the Gemini client
client = genai.Client(api_key=api_key)

# Send your first prompt to the AI model
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="What is happening in india today?"
)

# Print the AI response
print(response.text)