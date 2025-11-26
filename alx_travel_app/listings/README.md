# ALX Travel App 0x01

## Overview
This project is a Django-based travel booking platform. It demonstrates API development using Django REST Framework (DRF) and Swagger documentation. This milestone focuses on:

- Creating CRUD API endpoints for **Listings** and **Bookings**
- Implementing `ModelViewSet` in DRF
- Configuring RESTful API routes with routers
- Documenting endpoints with Swagger
- Testing API endpoints with Postman

## Project Structure

## API Endpoints

All API endpoints are under `/api/`.

### Listings

| Method | URL                     | Description             |
|--------|------------------------|-------------------------|
| GET    | /api/listings/          | List all listings       |
| POST   | /api/listings/          | Create a new listing    |
| GET    | /api/listings/{id}/     | Retrieve a listing      |
| PUT    | /api/listings/{id}/     | Update a listing        |
| DELETE | /api/listings/{id}/     | Delete a listing        |

### Bookings

| Method | URL                     | Description             |
|--------|------------------------|-------------------------|
| GET    | /api/bookings/          | List all bookings       |
| POST   | /api/bookings/          | Create a new booking    |
| GET    | /api/bookings/{id}/     | Retrieve a booking      |
| PUT    | /api/bookings/{id}/     | Update a booking        |
| DELETE | /api/bookings/{id}/     | Delete a booking        |

## Swagger Documentation

Swagger interactive API docs are available at:


## Testing

Use **Postman** or any API client to test GET, POST, PUT, DELETE requests.

---

## Notes

- All endpoints follow RESTful conventions.
- Ensure the server is running (`python manage.py runserver`) before testing.
