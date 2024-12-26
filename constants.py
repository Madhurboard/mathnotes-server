from dotenv import load_dotenv
import os

# Load environment variables from a .env file (useful for local development)
load_dotenv()

# Use environment variables for Render deployment
SERVER_URL = '0.0.0.0'
PORT = os.getenv('PORT', '8000')  # Default to 8000 if PORT is not set
ENV = os.getenv('ENV', 'prod')  # Default to 'prod' if ENV is not set

# Fetch the Gemini API key from environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable is not set!")
