from pydantic import BaseConfig

class Settings(BaseConfig):
    openai_api_key = str
    semantic_scholar_api_key: str or None = None
    pubmed_email: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()