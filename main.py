from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="StudentOS")

# In-memory storage (simple Python list)
# NOTE: Because this list is stored in computer memory (RAM),
# all data will reset whenever the server restarts.
subjects = []
subject_id_counter = 1


# Pydantic model to validate incoming subject data
class SubjectCreate(BaseModel):
    name: str = Field(..., min_length=1, description="Subject name (must not be empty)")
    code: str = Field(..., min_length=1, description="Subject code (must not be empty)")
    credits: int = Field(..., gt=0, description="Credits must be an integer greater than 0")


@app.get("/")
def read_root():
    """Check whether the API is running."""
    return {"message": "StudentOS is running!"}


@app.get("/subjects")
def get_subjects():
    """Return all subjects."""
    return subjects


@app.post("/subjects", status_code=status.HTTP_201_CREATED)
def create_subject(subject: SubjectCreate):
    global subject_id_counter
    new_subject = {
        "id": subject_id_counter,
        "name": subject.name,
        "code": subject.code,
        "credits": subject.credits,
    }
    subjects.append(new_subject)
    subject_id_counter += 1
    return new_subject


@app.get("/subjects/{subject_id}")
def get_subject(subject_id: int):
    for subject in subjects:
        if subject["id"] == subject_id:
            return subject
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Subject with ID {subject_id} not found",
    )


@app.delete("/subjects/{subject_id}")
def delete_subject(subject_id: int):
    for index, subject in enumerate(subjects):
        if subject["id"] == subject_id:
            subjects.pop(index)
            return {"message": f"Subject with ID {subject_id} deleted successfully."}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Subject with ID {subject_id} not found",
    )

