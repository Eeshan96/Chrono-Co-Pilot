import json
import os

MEMORY_FILE = "memory.json"
MAX_MESSAGES = 6

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return []

def save_memory(messages):
    # keep only last N messages
    trimmed = messages[-MAX_MESSAGES:]
    with open(MEMORY_FILE, "w") as f:
        json.dump(trimmed, f, indent=2)
