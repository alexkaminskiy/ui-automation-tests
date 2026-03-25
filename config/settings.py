from functools import lru_cache
from typing import Optional
from dataclasses import dataclass
import os
import yaml
from pathlib import Path


@dataclass
class Settings:
    base_url: str = "http://eaapp.somee.com/"
    browser: str = "chromium"
    headless: bool = True
    slowmo: int = 0
    timeout: int = 5000

    admin_username: Optional[str] = None
    admin_password: Optional[str] = None
    invalid_username: Optional[str] = None
    invalid_password: Optional[str] = None


def _load_from_yaml() -> dict:
    cfg_path = Path("config") / "settings.yaml"
    if not cfg_path.exists():
        return {}
    with cfg_path.open() as f:
        return yaml.safe_load(f) or {}


@lru_cache()
def get_settings() -> Settings:
    """Return Settings instance. Environment variables override YAML values."""
    data = _load_from_yaml()

    creds = data.get("credentials", {})

    s = Settings()

    # YAML values
    if "base_url" in data:
        s.base_url = data.get("base_url")
    if "browser" in data:
        s.browser = data.get("browser")
    if "headless" in data:
        s.headless = data.get("headless")
    if "slowmo" in data:
        s.slowmo = data.get("slowmo")
    if "timeout" in data:
        s.timeout = data.get("timeout")

    if creds:
        s.admin_username = creds.get("valid_user")
        s.admin_password = creds.get("valid_password")
        s.invalid_username = creds.get("invalid_user")
        s.invalid_password = creds.get("invalid_password")

    # Env vars override
    s.base_url = os.getenv("BASE_URL", s.base_url)
    s.browser = os.getenv("BROWSER", s.browser)
    s.headless = _coerce_bool(os.getenv("HEADLESS", str(s.headless)))
    s.slowmo = int(os.getenv("SLOWMO", s.slowmo))
    s.timeout = int(os.getenv("TIMEOUT", s.timeout))

    s.admin_username = os.getenv("AUTH_USER_NAME", s.admin_username)
    s.admin_password = os.getenv("AUTH_PASSWORD", s.admin_password)
    s.invalid_username = os.getenv("INVALID_USERNAME", s.invalid_username)
    s.invalid_password = os.getenv("INVALID_PASSWORD", s.invalid_password)

    return s


def _coerce_bool(val: str) -> bool:
    return str(val).lower() in ("1", "true", "yes", "y", "on")
