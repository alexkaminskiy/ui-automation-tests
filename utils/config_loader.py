import yaml
import os


def load_config(config_name: str = "settings") -> dict:
    path = os.path.join("config", f"{config_name}.yaml")
    with open(path, "r") as f:
        return yaml.safe_load(f)