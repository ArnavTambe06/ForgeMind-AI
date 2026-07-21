import json
import uuid
from datetime import datetime
from pathlib import Path

DATA_FILE = Path("data/projects.json")


def load_projects():
    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_projects(projects):
    with open(DATA_FILE, "w") as f:
        json.dump(projects, f, indent=4)


def create_project(name: str, description: str):

    projects = load_projects()

    project = {
        "id": str(uuid.uuid4()),
        "name": name,
        "description": description,
        "created_at": datetime.utcnow().isoformat()
    }

    projects.append(project)

    save_projects(projects)

    return project


def get_projects():
    return load_projects()


def delete_project(project_id: str):

    projects = load_projects()

    updated = [p for p in projects if p["id"] != project_id]

    save_projects(updated)