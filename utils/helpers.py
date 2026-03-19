import json
import os
from pathlib import Path
from typing import Tuple, Optional

from config.settings import get_settings



def get_user_credentials(key: str, path: str = "data/users.json") -> Tuple[Optional[str], Optional[str]]:
    """Resolve credentials preferring environment/Settings, then JSON file.

    Uses `config.settings.get_settings()` which prefers env vars and falls back to
    `config/settings.yaml`. If those don't contain the creds, the optional `data/users.json`
    file is used as a final fallback.
    """
    settings = get_settings()

    if key == "admin":
        if settings.admin_username or settings.admin_password:
            return settings.admin_username, settings.admin_password
    if key == "invalid":
        if settings.invalid_username or settings.invalid_password:
            return settings.invalid_username, settings.invalid_password

    # Fallback to JSON file
    p = Path(path)
    if p.exists():
        try:
            with p.open() as f:
                data = json.load(f)
            entry = data.get(key)
            if entry:
                return entry.get("username"), entry.get("password")
        except Exception:
            pass

    return None, None