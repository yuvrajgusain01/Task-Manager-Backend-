# Task Management REST API

A Task Management REST API built using Python and FastAPI. This project allows users to create, retrieve, update, and delete tasks through HTTP requests. It uses Pydantic for data validation, SQLAlchemy as the ORM, and PostgreSQL for persistent data storage.

## Features

- Create a new task
- Retrieve all tasks
- Retrieve a task by its ID
- Update an existing task
- Delete a task
- Validate task data using Pydantic
- Store and retrieve tasks from PostgreSQL
- Manage database operations using SQLAlchemy
- Handle tasks that do not exist
- Prevent duplicate task IDs and task names during creation
- Test API endpoints using Swagger UI

## Technologies Used

- **Python** – Programming language
- **FastAPI** – Web framework for building REST APIs
- **Pydantic** – Data validation and request model definition
- **SQLAlchemy** – ORM for interacting with the database
- **PostgreSQL** – Relational database for persistent storage
- **Psycopg** – PostgreSQL database driver
- **Uvicorn** – ASGI server for running the application
- **Swagger UI** – Interactive API documentation and testing

## Project Structure

```text
TaskManagement/
├── main.py
├── models.py
├── databaseModel.py
├── dbConfig.py
└── README.md
```

- `main.py` – Defines API endpoints and CRUD operations.
- `models.py` – Defines the Pydantic `Task` model for request validation.
- `databaseModel.py` – Defines the SQLAlchemy `Task` model and database table structure.
- `dbConfig.py` – Configures the PostgreSQL connection, SQLAlchemy engine, and session factory.
- `README.md` – Project documentation.

## Installation and Setup

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd TaskManagement
```

### 2. Create a virtual environment

```bash
python -m venv myenv
```

Activate it on Windows PowerShell:

```powershell
.\myenv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install fastapi uvicorn sqlalchemy "psycopg[binary]"
```

### 4. Configure PostgreSQL

Make sure PostgreSQL is installed and running.

Create a database named `TaskManagement` using PostgreSQL.

Configure the database connection in `dbConfig.py` with your PostgreSQL username, password, host, port, and database name.

**Security note:** Do not commit database passwords or other secrets to your Git repository. Use environment variables to store credentials in real projects.

### 5. Run the application

```bash
uvicorn main:app --reload
```

The API will be available at:

- API base URL: http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/tasks` | Retrieve all tasks |
| GET | `/tasks/{taskId}` | Retrieve a task by ID |
| POST | `/task` | Create a new task |
| PUT | `/task/{taskId}` | Update an existing task |
| DELETE | `/task/{taskId}` | Delete a task |

## Example Task

Send the following JSON body to `POST /task`:

```json
{
  "taskId": 1,
  "taskName": "Running",
  "taskDescription": "Running is a cardio exercise"
}
```

Example successful response:

```json
{
  "taskId": 1,
  "taskName": "Running",
  "taskDescription": "Running is a cardio exercise"
}
```

The task is stored in PostgreSQL and remains available after the server restarts.

## Testing with Swagger UI

FastAPI provides an interactive Swagger UI for testing API endpoints.

1. Start the application.
2. Open http://127.0.0.1:8000/docs.
3. Select an endpoint.
4. Click **Try it out**.
5. Enter the required parameters or JSON request body.
6. Click **Execute** to view the response.

Test the CRUD operations in the following order:

1. Create a task using `POST /task`.
2. Retrieve all tasks using `GET /tasks`.
3. Retrieve an individual task using `GET /tasks/{taskId}`.
4. Update a task using `PUT /task/{taskId}`.
5. Delete a task using `DELETE /task/{taskId}`.

## Database and Storage

This project uses PostgreSQL to store task records persistently.

SQLAlchemy maps Python classes to database tables and provides methods for querying, inserting, updating, and deleting records.

The application uses SQLAlchemy sessions to manage database transactions. Unlike in-memory storage, PostgreSQL data is not automatically lost when the FastAPI server restarts.

The database table is defined in `databaseModel.py`, while `models.py` contains the Pydantic model used to validate incoming request data.

## Learning Objectives

- Understand REST API principles and HTTP methods.
- Learn how FastAPI handles requests and responses.
- Use Pydantic for request data validation.
- Implement CRUD operations.
- Understand SQLAlchemy ORM and database sessions.
- Connect a FastAPI application to PostgreSQL.
- Understand the difference between Pydantic models and SQLAlchemy models.
- Test API endpoints using Swagger UI.
- Understand persistent storage versus in-memory storage.

## License

This project is intended for learning and educational purposes.
