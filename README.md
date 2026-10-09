# StudentOS 🎓

> A beginner-friendly, all-in-one academic productivity platform built with Python and FastAPI.

*Status: In Active Development 🚧*

---

## 📌 Problem Statement

College life is notoriously fragmented. Students frequently juggle multiple disjointed tools, spreadsheets, and physical notebooks to keep track of their day-to-day academic responsibilities.

Managing courses, monitoring assignment deadlines, calculating attendance percentages, organizing study schedules, tracking student expenses, and reviewing overall academic performance often leads to cognitive overload and missed deadlines.

**StudentOS** is being designed to solve this fragmentation by providing a single, unified, student-first productivity platform that consolidates essential academic workflows into an intuitive and structured system.

---

## 🎯 Project Goals

The objective of StudentOS is to build modular services tailored to university life. Planned core features include:

* **Subject Management**: Organize course details, course codes, syllabus info, and credit counts.
* **Assignment Tracking**: Manage assignments, lab submissions, priority levels, and approaching deadlines.
* **Attendance Tracking**: Log class sessions, calculate minimum attendance criteria, and receive low-attendance warnings.
* **Study Planner**: Create daily study goals, revision blocks, and exam prep schedules.
* **Expense Tracker**: Monitor student budgets, essential college expenses, and recurring subscriptions.
* **Academic Analytics**: Track GPA/CGPA milestones, semester progress, and overall academic performance.

---

## 🛠️ Tech Stack

### Currently Used
* **Backend**: [Python](https://www.python.org/)
* **API Framework**: [FastAPI](https://fastapi.tiangolo.com/)
* **Data Validation**: [Pydantic](https://docs.pydantic.dev/)
* **Server**: [Uvicorn](https://www.uvicorn.org/)
* **Version Control**: Git & GitHub

### Planned Technologies
* **Database**: SQLite with SQLAlchemy ORM (for persistent local data storage)
* **Frontend**: Modern web interface (for an interactive browser dashboard)
* **Authentication**: User authentication & session management

---

## 🚀 Current Progress

StudentOS has a working **FastAPI backend** with the following functional endpoints:

* `GET /` — Health check endpoint returning `{"message": "StudentOS is running!"}`
* `GET /subjects` — Retrieve all subjects (returns an empty list `[]` if none exist)
* `POST /subjects` — Create a new subject with Pydantic validation (`name`, `code`, `credits > 0`) and an auto-assigned ID
* `GET /subjects/{subject_id}` — Retrieve a specific subject by ID (returns HTTP 404 if not found)
* `DELETE /subjects/{subject_id}` — Delete a specific subject by ID (returns HTTP 404 if not found)

> **⚠️ Storage Note**: Subject data is currently stored in an **in-memory Python list** and resets whenever the server restarts. Persistent storage using **SQLite** is planned, not implemented.

---

## 💻 Getting Started (Windows PowerShell)

Follow these step-by-step instructions to set up and run the backend locally using Windows PowerShell.

### 1. Prerequisites
Ensure you have cloned the repository and navigated to the project root:
```powershell
cd c:\Users\HP\Documents\Projects\studentos
```

### 2. Activate the Virtual Environment
Activate the existing virtual environment (`.venv`) in PowerShell:
```powershell
.\.venv\Scripts\Activate.ps1
```

> **Note**: If PowerShell displays an `ExecutionPolicy` error when running the script, enable script execution for your current session:
> ```powershell
> Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
> ```

### 3. Run the Development Server
Start the FastAPI server with live reload enabled using Python's module runner:
```powershell
python -m uvicorn main:app --reload
```

Using `python -m uvicorn` ensures the command executes using the Python interpreter and packages installed inside your activated `.venv`.

The server will start at:
* **Local Server**: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### 4. Interactive API Documentation
While the server is running, FastAPI automatically generates interactive OpenAPI documentation. You can test and inspect all endpoints directly in your browser:
* **Swagger UI Docs**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc Alternate Docs**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🗺️ Roadmap

- [x] **Phase 1: Project Setup & Core API Foundation**
  - [x] FastAPI project initialization and health check (`GET /`)
  - [x] Environment configuration with virtual environment (`.venv`)
  - [x] Interactive OpenAPI/Swagger documentation setup
- [x] **Phase 2: Subject Management CRUD (Current In-Memory Version)**
  - [x] Pydantic schema validation (`SubjectCreate` with `name`, `code`, `credits`)
  - [x] `GET /subjects` — List all subjects
  - [x] `POST /subjects` — Create subject with auto-increment ID
  - [x] `GET /subjects/{subject_id}` — Retrieve subject by ID with 404 handling
  - [x] `DELETE /subjects/{subject_id}` — Delete subject by ID with 404 handling
- [ ] **Phase 3: Database Integration (Planned)**
  - [ ] Configure SQLite database and SQLAlchemy ORM
  - [ ] Implement database migrations
  - [ ] Migrate in-memory subjects to persistent SQLite storage
- [ ] **Phase 4: Additional Core Academic Modules (Planned)**
  - [ ] Assignment & Task Tracker with due dates and priority
  - [ ] Attendance Calculator & tracker with low-attendance warnings
- [ ] **Phase 5: Productivity & Financial Utilities (Planned)**
  - [ ] Study schedule & revision planner
  - [ ] Student budget & expense logger
  - [ ] Academic analytics & GPA tracker
- [ ] **Phase 6: Frontend & Authentication (Planned)**
  - [ ] User authentication and session management
  - [ ] Clean, responsive web dashboard

---

## 🧠 Learning Outcomes

Building StudentOS provides practical experience with modern software engineering practices, including:

* **RESTful API Design**: Structuring clean HTTP methods (`GET`, `POST`, `PUT`, `DELETE`), status codes, and path parameters.
* **Data Validation with Pydantic**: Enforcing strict schema validation and structured error reporting.
* **FastAPI Architecture**: Leveraging dependency injection, type annotations, and automated OpenAPI documentation.
* **Environment & Package Management**: Managing isolated Python virtual environments (`.venv`) and dependencies.
* **Git Workflow**: Managing feature branches, descriptive commit histories, and professional repository documentation.
