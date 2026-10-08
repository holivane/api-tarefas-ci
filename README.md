# Tasks API

A small REST API built with Flask to manage tasks. Built step by step, test-first.

## Current features

- `GET /health`: health check, returns `{"status": "ok"}`
- `POST /tasks`: creates a task, returns it with status `201`
- `GET /tasks`: lists all tasks

Tasks are stored in memory, so they are lost when the server restarts.

## Requirements

- Python 3.10+
- pip

## Setup

```bash
# Create and activate the virtual environment
python -m venv venv
source venv/bin/activate        # Linux/macOS/Git Bash
# venv\Scripts\Activate.ps1     # Windows PowerShell

# Install dependencies
pip install flask pytest
```

## Running the server

```bash
flask --app app run
```

The API will be available at `http://localhost:5000`.

## Usage examples

```bash
# Health check
curl http://localhost:5000/health

# Create a task
curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Study Flask"}'

# List tasks
curl http://localhost:5000/tasks
```

Example response for `POST /tasks`:

```json
{"id": 1, "title": "Study Flask"}
```

## Running the tests

```bash
pytest -v
```

The tests use Flask's test client, so the server does not need to be running.

## Project structure

```
.
├── app.py          # Flask application and routes
├── test_app.py     # Tests (pytest)
├── .gitignore
└── README.md
```

## Next steps

- Validate input (e.g. missing `title`)
- Add more routes (get, update and delete a single task)
- Set up continuous integration