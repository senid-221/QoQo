from pydantic_settings import BaseSettings
from pathlib import Path
import secrets


class Settings(BaseSettings):
    dashscope_api_key: str = ""
    dashscope_base_url: str = "https://dashscope.aliyuncs.com/compatible-mode/v1"
    model_name: str = "qwen-plus"

    max_tokens: int = 8192
    temperature: float = 0.2
    max_tool_rounds: int = 8

    workspace_dir: str = str(Path(__file__).parent.parent / "workspace")
    data_dir: str = str(Path(__file__).parent / "data")

    jwt_secret: str = secrets.token_urlsafe(32)
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 60 * 24 * 7

    github_client_id: str = ""
    github_client_secret: str = ""
    google_client_id: str = ""
    google_client_secret: str = ""

    public_base_url: str = "http://localhost:8000"
    frontend_url: str = "http://localhost:5173"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"


settings = Settings()

Path(settings.workspace_dir).mkdir(parents=True, exist_ok=True)
Path(settings.data_dir).mkdir(parents=True, exist_ok=True)
(Path(settings.data_dir) / "users").mkdir(parents=True, exist_ok=True)
(Path(settings.data_dir) / "conversations").mkdir(parents=True, exist_ok=True)
