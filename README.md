# Taskify

Taskify is a simple task management API built with FastAPI. It supports user registration, login, and task management with automatic tagging using NLP.

## Features

- User registration and authentication
- Add, complete, and delete tasks
- Automatic tag suggestion for tasks using NLP
- Persistent storage with JSON files

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/taskify.git
   cd taskify
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python -m venv .myenv
   source .myenv/Scripts/activate  # On Windows
   # Or
   source .myenv/bin/activate      # On Linux/Mac
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Download NLTK data (if needed):**
   ```python
   import nltk
   nltk.download('stopwords')
   nltk.download('wordnet')
   nltk.download('punkt')
   ```

## Running the API

Start the FastAPI server using Uvicorn:

```sh
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000/`.

## API Endpoints

### Home

- **GET /**  
  Returns a welcome message.

### Register

- **POST /register**  
  **Parameters:**  
  - `username`: string  
  - `password`: string  
  **Response:**  
  - Success or error message

### Login

- **POST /login**  
  **Parameters:**  
  - `username`: string  
  - `password`: string  
  **Response:**  
  - `success`: bool  
  - `username`: string or null

### Add Task

- **POST /add_task**  
  **Parameters:**  
  - `username`: string  
  - `content`: string  
  **Response:**  
  - `task`: Task object (with suggested tags)

### Get Tasks

- **GET /tasks**  
  **Parameters:**  
  - `username`: string  
  **Response:**  
  - `tasks`: List of tasks for the user

## Data Storage

- Users are stored in [`data/users.json`](data/users.json)
- Tasks are stored in [`data/tasks.json`](data/tasks.json)

## Project Structure

```
main.py
app/
  managers/
    user_manager.py
    task_manager.py
  models.py
  tagger.py
  utils/
    json_helper.py
data/
  users.json
  tasks.json
requirements.txt
```

## Example Usage

Register a user:
```sh
curl -X POST "http://127.0.0.1:8000/register?username=testuser&password=testpass"
```

Login:
```sh
curl -X POST "http://127.0.0.1:8000/login?username=testuser&password=testpass"
```

Add a task:
```sh
curl -X POST "http://127.0.0.1:8000/add_task?username=testuser&content=Finish the FastAPI backend"
```

Get tasks:
```sh
curl "http://127.0.0.1:8000/tasks?username=testuser"
```

## License

MIT

---

Made with ❤️ using FastAPI and NLP.