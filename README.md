# Blog API

A web service project for creating and managing blog posts with user authentication, built using **FastAPI** and **SQLAlchemy**.

## Features
- **User Registration**: Sign up with name, email, and password.
- **Authentication**: Secure login with JWT token.
- **CRUD Operations for Blogs**: Create, retrieve, update, and delete blog posts.
- **User-Blog Relationship**: Each blog post is associated with a registered user.
- **Protected Routes**: Only authenticated users can create, update, or delete blogs.

## Technologies Used
- Python 3.12
- FastAPI
- SQLAlchemy
- OAuth2 with JWT tokens
- SQLite

## Getting Started

### Installation
1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-folder>
```
2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate    # For Windows
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application
Start the FastAPI server:
```bash
uvicorn blog.main:app --reload
```

The application will be accessible at: `http://127.0.0.1:8000`

### API Overview
- **POST /login**: Authenticate user and receive a JWT token.
- **POST /users/**: Register a new user.
- **GET /users/**: Retrieve all users.
- **GET /users/{id}**: Retrieve a user by ID.
- **POST /blogs/**: Create a new blog post (requires authentication).
- **GET /blogs/**: Retrieve all blog posts (requires authentication).
- **GET /blogs/{id}**: Retrieve a blog post by ID (requires authentication).
- **PUT /blogs/{id}**: Update a blog post (requires authentication).
- **DELETE /blogs/{id}**: Delete a blog post (requires authentication).

> To access protected routes, include the JWT token in the request headers:
```http
Authorization: Bearer <your_token>

### Screenshots 📸
![image](https://github.com/user-attachments/assets/628a517e-e169-436d-8d85-94262290a3e8)





