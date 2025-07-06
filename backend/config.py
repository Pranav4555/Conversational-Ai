
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="bot.env")  


GOOGLE_CALENDAR_ID = os.getenv("GOOGLE_CALENDAR_ID")
GOOGLE_CREDENTIALS_PATH = os.getenv("GOOGLE_CREDENTIALS_PATH")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
