from fastapi import APIRouter, HTTPException
from uuid import uuid4
from datetime import datetime

projects = []

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)


@router.post("/")
def create_project(project: dict):

    new_project = {
        "id": str(uuid4()),
        "name": project.get("name"),
        "description": project.get("description"),
        "created_at": datetime.utcnow().isoformat()
    }

    projects.append(new_project)

    return new_project


@router.get("/")
def get_projects():
    return projects


@router.get("/{project_id}")
def get_project(project_id: str):

    for project in projects:
        if project["id"] == project_id:
            return project

    raise HTTPException(status_code=404, detail="Project not found")


@router.delete("/{project_id}")
def delete_project(project_id: str):

    for project in projects:
        if project["id"] == project_id:
            projects.remove(project)
            return {"message": "Deleted successfully"}

    raise HTTPException(status_code=404, detail="Project not found")