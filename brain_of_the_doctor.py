# Step 0: Import required libraries
import os
from dotenv import load_dotenv
from groq import Groq
import base64

# Step 1: Load environment variables from .env file
load_dotenv()  # This loads variables from a .env file in your project directory

# Step 2: Get the API key with better error handling
try:
    GROQ_API_KEY = os.environ["GROQ_API_KEY"]  # Using [] instead of get() for better error reporting
except KeyError:
    raise RuntimeError(
        "GROQ_API_KEY not found. Please create a .env file with your API key or "
        "set it as an environment variable. See instructions in the README."
    )

# Step 3: Convert Image to required format with error handling
# image_path = "acne.jpeg"
def encode_image(image_path):

    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except FileNotFoundError:
        raise FileNotFoundError(
            f"Image file not found at path: {image_path}. "
            "Please ensure the image exists in the correct location."
        )
    except Exception as e:
        raise RuntimeError(f"Error processing image: {str(e)}")

# Step 4: Setup and query the Groq client
query = "Is there something wrong with my face?"
model = "meta-llama/llama-4-scout-17b-16e-instruct"

def analyze_image_with_query(query, model,encoded_image):
    client = Groq(api_key=GROQ_API_KEY)
    messages = [{
        "role": "user",
        "content": [
            {"type": "text", "text": query},
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"},
            },
        ],
    }]

    try:
        print("Sending request to Groq API...")
        chat_completion = client.chat.completions.create(
            messages=messages,
            model=model
        )
        print("\nResponse received:")
        print(chat_completion.choices[0].message.content)
        return chat_completion.choices[0].message.content

        
    except Exception as e:
        raise RuntimeError(f"Error communicating with Groq API: {str(e)}")