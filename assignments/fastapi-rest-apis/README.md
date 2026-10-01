# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API using FastAPI to practice creating endpoints, handling JSON data, and validating inputs in a web application.

## 📝 Tasks

### 🛠️ Create a FastAPI App

#### Description
Set up a basic FastAPI application and create your first API endpoint that returns JSON data.

#### Requirements
Completed program should:

- Install and import the `fastapi` package
- Create a FastAPI app instance
- Add a root endpoint that responds with a welcome message
- Return JSON data in a clean and readable format
- Use a local development server to test the endpoint
- Example output:
  ```python
  @app.get("/")
  def read_root():
      return {"message": "Welcome to the Task API"}
  ```

### 🛠️ Build Todo Endpoints

#### Description
Create endpoints for listing tasks and adding new tasks to an in-memory collection.

#### Requirements
Completed program should:

- Define a list of sample tasks in memory
- Add a `GET /items` endpoint that returns all tasks
- Add a `POST /items` endpoint that accepts new task data
- Return the created item in JSON format
- Keep the API response structure simple and consistent
- Example output:
  ```json
  [{"id": 1, "name": "Write code", "done": false}]
  ```

### 🛠️ Add Validation and Error Handling

#### Description
Improve the API by validating incoming data and handling missing resources gracefully.

#### Requirements
Completed program should:

- Use a Pydantic model to validate task fields
- Enforce required fields such as `name` and `done`
- Add a `GET /items/{item_id}` endpoint
- Return a `404` response when a task is not found
- Display clear JSON error messages for invalid requests
- Example output:
  ```json
  {"detail": "Item not found"}
  ```
