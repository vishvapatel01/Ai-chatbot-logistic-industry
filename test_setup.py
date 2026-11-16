from config import Config, get_groq_client
from prompts import SYSTEM_PROMPT

if __name__ == "__main__":
    try:
        client = get_groq_client()
        print("Groq client initialized successfully.")
        print(f"Configured Model: {Config.MODEL_NAME}")
        print(f"System Prompt Loaded: {len(SYSTEM_PROMPT)} characters")
    except ValueError as e:
        print(f"Configuration Error: {e}")