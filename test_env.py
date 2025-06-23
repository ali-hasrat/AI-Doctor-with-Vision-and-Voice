from dotenv import load_dotenv
import os

# Load the .env file from current directory
result = load_dotenv(dotenv_path=".env")
print("✅ dotenv loaded:", result)

# Check value
api_key = os.getenv("GROQ_API_KEY")
if api_key:
    print("✅ API Key loaded:", api_key[:6] + "..." + api_key[-6:])
else:
    print("❌ API Key NOT loaded.")


from dotenv import load_dotenv
import os

# Load the .env file from current directory
result = load_dotenv(dotenv_path=".env")
print("✅ dotenv loaded:", result)

# Check value
api_key = os.getenv("ELEVENLABS_API_KEY")
if api_key:
    print("✅ API Key loaded:", api_key[:6] + "..." + api_key[-6:])
else:
    print("❌ API Key NOT loaded.")
