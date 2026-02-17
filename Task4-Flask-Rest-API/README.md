# Task 4 - Flask REST API

## Objective
Build a REST API using Flask to manage user data.

## Tools Used
- Python 3.11
- Flask
- Postman

## Features
- GET all users
- GET single user
- POST new user
- PUT update user
- DELETE user
- In-memory storage using dictionary

## Setup Instructions

1. Clone repository
2. Create virtual environment:
   py -3.11 -m venv venv

3. Activate environment:
   venv\Scripts\activate

4. Install dependencies:
   pip install -r requirements.txt

5. Run app:
   python app.py

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|------------|
| GET | /users | Get all users |
| GET | /users/<id> | Get single user |
| POST | /users | Add user |
| PUT | /users/<id> | Update user |
| DELETE | /users/<id> | Delete user |

## Concepts Used
- REST
- HTTP Methods
- JSON
- Flask Routing
- Status Codes (200, 201, 400, 404)

