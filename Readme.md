# Task Management REST API

A simple Task Management REST API built using Python and FastAPI. This project allows users to create, view, update, and delete tasks using HTTP requests. It uses Pydantic for data validation and in-memory storage to manage tasks without a database.

## Features

- Create a new task
- Retrieve all tasks
- Retrieve a task by its ID
- Update an existing task
- Delete a task
- Validate task data using Pydantic
- Handle tasks that do not exist
- Test API endpoints using Swagger UI
- Store tasks in memory without requiring a database

## Technologies Used

- **Python** – Programming language
- **FastAPI** – Web framework for building REST APIs
- **Pydantic** – Data validation and model definition
- **Uvicorn** – ASGI server for running the application
- **Swagger UI** – Interactive API testing

## Project Structure

```text
TaskManagement/
├── main.py
├── models.py
└── README.md
```

- `main.py` – Defines the API endpoints and CRUD operations.
- `models.py` – Defines the Task model using Pydantic.
- `README.md` – Project documentation.

## Installation and Setup

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd TaskManagement
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn
```

### 4. Run the application

```bash
uvicorn main:app --reload
```

The API will run at:

`http://127.0.0.1:8000`

## API Endpoints

| Method | Endpoint            | Description                                    |
| ------ | ------------------- | ---------------------------------------------- |
| GET    | `/tasks`            | Retrieve all tasks                             |
| GET    | `/tasks/{taskId}`   | Retrieve a task by ID                          |
| POST   | `/task`             | Create a new task                              |
| PUT    | `/task?Id={id}`     | Update an existing task                        |
| DELETE | `/task?taskId={id}` | Delete a task                                  |
| POST   | `/input-task`       | Enter task details through the server terminal |

## Example Task

Send the following JSON body to `POST /task`:

```json
{
  "taskId": 1,
  "taskName": "Running",
  "taskDescription": "Running is a cardio exercise"
}
```

## Testing with Swagger UI

FastAPI provides an interactive Swagger UI to test API endpoints.

1. Start the application.
2. Open `http://127.0.0.1:8000/docs`.
3. Select an endpoint.
4. Click **Try it out**.
5. Enter the required parameters or JSON data.
6. Click **Execute** to view the response.

## Storage

This project uses an in-memory Python list to store tasks. No database is required.

**Note:** Tasks are temporary and will be lost when the server restarts. The project can later be extended with a database such as PostgreSQL or MySQL.

## Learning Objectives

- Understand REST API principles and HTTP methods.
- Learn how FastAPI handles requests and responses.
- Use Pydantic to validate incoming data.
- Implement CRUD operations.
- Test API endpoints using Swagger UI.
- Understand the difference between in-memory storage and database persistence.

## License

This project is intended for learning and educational purposes.
