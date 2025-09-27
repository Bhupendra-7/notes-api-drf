# Notes API

A RESTful API for managing notes built with Django and Django REST Framework (DRF).  
This API supports user authentication, note creation, updating, deletion, and filtering notes by priority.

## Features

- User signup and token-based authentication
- CRUD operations on notes (Create, Read, Update, Delete)
- Notes are owned by users — only owners can view or modify their notes
- Filter notes by priority (high, medium, low) for authenticated users
- Public endpoint to view all notes (unauthenticated users)
- Secure permissions and validation

## Technologies Used

- Python 3.x
- Django 4.x
- Django REST Framework
- PostgreSQL
- Token Authentication
- Postman (for API testing)

## Getting Started

### Prerequisites

- Python 3.6+
- Git
- Virtualenv (recommended)

### Installation

1. Clone the repository

```bash
git clone https://github.com/Bhupendra-7/notes-api-drf.git
```
2. Create and activate virtual environment
   python -m venv nenv
# On Windows
  nenv\Scripts\activate
# On macOS/Linux
  source nenv/bin/activate

3. Install dependencies
   pip install -r requirements.txt

4. Run migrations
   python manage.py migrate

5. Create a superuser (optional)
   python manage.py createsuperuser

6. Run the development server
   python manage.py runserver

Filtering Notes by Priority
Authenticated users can filter their notes by priority using query parameters:
Example: GET /api/notes/?priority=high
Unauthenticated users get all notes regardless of the priority filter.

Testing
You can use Postman or similar API clients to test the endpoints. Remember to include the token in the Authorization header for protected routes:
Authorization: Token your_token_here


  



