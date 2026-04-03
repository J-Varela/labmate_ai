# LabMate AI

LabMate AI is a monorepo with separate backend and frontend applications.

## Repository Structure

- `backend/`: FastAPI backend service and API routes
- `frontend/`: Frontend application

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/J-Varela/labmate_ai.git
cd labmate_ai
```

### 2. Run the backend

```bash
cd backend
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Backend default URL: `http://127.0.0.1:8000`

### 3. Run the frontend

Set up and run the frontend inside the `frontend/` folder based on your frontend stack.

## Notes

- Keep backend code in `backend/`.
- Keep frontend code in `frontend/`.
- Keep project-wide docs and config files in the repository root.
