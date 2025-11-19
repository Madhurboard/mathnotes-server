from dotenv import load_dotenv
import os

load_dotenv()

SERVER_URL = '0.0.0.0'
PORT = os.getenv('PORT', '8000')
ENV = os.getenv('ENV', 'prod')

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    print("[WARN] GEMINI_API_KEY environment variable is not set. The analyze endpoint will be disabled.")

