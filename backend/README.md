# LabMate AI Backend

FastAPI backend for managing experiments, recording trials, and generating experiment summaries.

## Stack

- FastAPI
- SQLAlchemy
- PostgreSQL driver via `psycopg2-binary`
- Pydantic settings

## Prerequisites

- Python 3.10+
- A database connection string exposed as `DATABASE_URL`

## Installation

From the `backend` directory:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in `backend/`:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/labmate_ai
```

Current settings:

- `APP_NAME` defaults to `LabMate AI API`
- `DATABASE_URL` is required for startup

## Running the API

From the `backend` directory:

```bash
uvicorn app.main:app --reload
```

The API starts with:

- Root endpoint at `GET /`
- Health check at `GET /api/v1/health`
- Interactive docs at `GET /docs`

## API Routes

Base prefix: `/api/v1`

### Experiments

- `POST /experiments` creates an experiment
- `GET /experiments` lists experiments ordered by newest first
- `GET /experiments/{experiment_id}` fetches a single experiment

### Trials

- `POST /experiments/{experiment_id}/trials` creates a trial for an experiment
- `GET /experiments/{experiment_id}/trials` lists trials for an experiment

### AI Summary

- `POST /experiments/{experiment_id}/summarize` generates a text summary from the experiment and its trials

## Notes

- Tables are created on application startup via SQLAlchemy metadata.
- The current summary flow is local and rule-based; it does not call an external AI provider.
- `alembic` is listed as a dependency, but this repository currently relies on automatic table creation in `app.main`.
