# Loads the execution path, language and any other information that executor.py might need
import json
from pathlib import Path
from .display import Message

def load_module(category, module):
    path = Path("modules") / category / module / "module.json"
    try:
        with open(path) as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        Message._print("error", f"Module '{category}/{module}' not found")
    except json.JSONDecodeError as e:
        Message._print("error", f"Failed to parse module.json for '{category}/{module}': {e}")
