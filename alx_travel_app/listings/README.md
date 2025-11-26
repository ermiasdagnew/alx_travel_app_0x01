# ALX Travel App - 0x01 API Development

## Overview
This project extends the ALX Travel App by adding full CRUD API endpoints for **Listings** and **Bookings** using Django REST Framework (DRF).  
It also integrates **Swagger documentation** for easy testing and exploration of the API.

## Features
- CRUD operations for Listings
- CRUD operations for Bookings
- DRF ModelViewSets for clean and reusable code
- Automatic URL routing using DRF Routers
- Swagger UI documentation using drf-yasg
- Postman-tested API endpoints

## API Endpoints
| Resource  | Method | Endpoint           | Description            |
|-----------|--------|--------------------|------------------------|
| Listings  | GET    | `/api/listings/`   | List all listings      |
| Listings  | POST   | `/api/listings/`   | Create a listing       |
| Listings  | GET    | `/api/listings/<id>/` | Retrieve listing   |
| Listings  | PUT    | `/api/listings/<id>/` | Update listing     |
| Listings  | DELETE | `/api/listings/<id>/` | Delete listing     |
| Bookings  | Same pattern as above | `/api/bookings/` | CRUD for bookings |

## Technologies Used
- Django 4.x
- Django REST Framework
- drf-yasg (Swagger documentation)
- SQLite/PostgreSQL (depending on your setup)

## Swagger Documentation
After running the server:

This displays interactive API documentation.

## Instructions
- Duplicate project from `alx_travel_app_0x00`
- Implement ViewSets in `listings/views.py`
- Configure router in `listings/urls.py`
- Test endpoints with Postman
