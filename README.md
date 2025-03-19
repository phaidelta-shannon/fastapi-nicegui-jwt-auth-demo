# FastAPI + NiceGUI JWT Auth Demo

A simple demo API built with FastAPI and NiceGUI, implementing JWT-based authentication with in-memory user storage. This project follows best practices for token-based authentication and serves as a reference for integrating JWT with FastAPI and NiceGUI.

## Features

- JWT-based authentication
- In-memory user storage (no database)
- Protected endpoints using JWT tokens
- Built with FastAPI and NiceGUI

## Project Structure
```
fastapi-nicegui-jwt-auth-demo/
|
├── backend/
│   ├── main.py
│   ├── auth.py
│   └── models.py
|
├── frontend/
│   └── app.py
|
├── .env
├── requirements.txt
├── README.md
└── .gitignore
```

## Setup Instructions

1. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   ```
2. **Activate the Virtual Environment**:
   ```bash
   venv\Scripts\activate
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Backend Server**:
   ```bash
   uvicorn backend.main:app --reload
   ```
5. **Run the Frontend Application:**:
   ```bash
   python frontend/app.py
   ```

## API Endpoints
```POST /token```: Get a JWT token by providing username and password.

```GET /users/me/```: Access user details (protected by JWT).

```GET /users/me/items/```: Access user-specific items (protected by JWT).

## Testing the API
Get a token:
```
curl -X POST "http://127.0.0.1:8000/token" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "username=johndoe&password=secret"
```

Access a protected endpoint
```
curl -X GET "http://127.0.0.1:8000/users/me/" -H "accept: application/json" -H "Authorization: Bearer <your_token>"
```