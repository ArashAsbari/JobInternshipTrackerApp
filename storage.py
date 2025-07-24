import json
import os

DATA_FILE = "jobs_data.json"

def save_jobs(jobs):
    """Save the list of job entries to a JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(jobs, f, indent=4)

def load_jobs():
    """Load job entries from a JSON file. Returns an empty list if the file doesn't exist."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)
