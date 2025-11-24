# ALX Travel App

This Django REST Framework project provides CRUD API endpoints for managing travel listings and bookings. It also includes Swagger documentation for easy API exploration.

## Features

- Manage travel listings (Create, Read, Update, Delete)
- Manage bookings for listings
- API documentation via Swagger
- Fully testable endpoints via Postman or Swagger UI

## API Endpoints

- `/api/listings/` - CRUD operations for listings
- `/api/bookings/` - CRUD operations for bookings
- `/swagger/` - Interactive API docs

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
