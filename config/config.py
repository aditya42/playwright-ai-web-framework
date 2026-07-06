import os
from dataclasses import dataclass
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LOCAL_APP_URL = (PROJECT_ROOT / "tests" / "fixtures" / "saucedemo_mock.html").as_uri()

@dataclass(frozen=True)
class Settings:
    base_url: str = os.getenv("BASE_URL", DEFAULT_LOCAL_APP_URL)
    browser: str = os.getenv("BROWSER", "chromium")
    headless: bool = os.getenv("HEADLESS", "true").lower() == "true"
    slow_mo: int = int(os.getenv("SLOW_MO", "0"))
    timeout: int = int(os.getenv("TIMEOUT", "30000"))
    username: str = os.getenv("SAUCE_USERNAME", "standard_user")
    password: str = os.getenv("SAUCE_PASSWORD", "secret_sauce")
    openai_api_key: str | None = os.getenv("OPENAI_API_KEY")
    chromium_executable_path: str | None = os.getenv("CHROMIUM_EXECUTABLE_PATH")

settings = Settings()
