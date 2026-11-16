import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from the .env file
load_dotenv()

class Config:
    """Configuration class for LLM and application settings."""
    
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")
    # Recommended fast, high-accuracy model on Groq for structured RAG/KB tasks
    MODEL_NAME: str = "llama-3.3-70b-versatile"
    TEMPERATURE: float = 0.1  # Low temperature to enforce factual, deterministic responses
    MAX_TOKENS: int = 1024

    @classmethod
    def validate(cls) -> None:
        """Validates that critical environment variables are set."""
        if not cls.GROQ_API_KEY:
            raise ValueError(
                "GROQ_API_KEY is missing. Please set it in your .env file or system environment variables."
            )

def get_groq_client() -> Groq:
    """Validates configuration and returns an initialized Groq client."""
    Config.validate()
    return Groq(api_key=Config.GROQ_API_KEY)