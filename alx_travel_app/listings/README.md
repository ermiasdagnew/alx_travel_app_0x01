# ✈️ ALX Travel App: Listings and Bookings API (`alx_travel_app_0x01`)

This project is an iteration of the ALX Travel App, focused on implementing a robust, documented RESTful API using the Django REST Framework (DRF) to manage property listings and user bookings.

## 🎯 Objective

To build and document API views for managing `Listing` and `Booking` resources, ensuring all endpoints follow RESTful conventions and are accessible under the `/api/` base path.

## 🛠️ Setup and Installation

### Prerequisites

* Python 3.8+
* Django (latest stable version)
* Django REST Framework
* `drf-spectacular` (for Swagger/OpenAPI documentation)

### Steps

1.  **Clone or Duplicate the Project:**
    ```bash
    git clone <your_repo_url> alx_travel_app_0x01
    cd alx_travel_app_0x01/alx_travel_app
    ```

2.  **Setup Virtual Environment & Install Dependencies:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt # or manually install django djangorestframework drf-spectacular
    ```

3.  **Database Migration:**
    ```bash
    python manage.py makemigrations listings
    python manage.py migrate
    python manage.py createsuperuser # Recommended for testing authenticated endpoints
    ```

4.  **Run the Server:**
    ```bash
    python manage.py runserver
    ```

---

## 🌐 API Endpoints

All API endpoints are configured using the DRF `DefaultRouter` and are accessible under the base URL: `http://127.0.0.1:8000/api/`

### Listings Management (`listings/`)

Managed by `listings.views.ListingViewSet`.

| Method | Endpoint | Description | Authentication |
| :--- | :--- | :--- | :--- |
| `GET` | `/api/listings/` | List all available listings. | None (Public) |
| `POST` | `/api/listings/` | Create a new property listing. | Required |
| `GET` | `/api/listings/{pk}/` | Retrieve details for a specific listing. | None (Public) |
| `PUT/PATCH`| `/api/listings/{pk}/` | Update an existing listing. | Required |
| `DELETE` | `/api/listings/{pk}/` | Remove a listing. | Required |

### Bookings Management (`bookings/`)

Managed by `listings.views.BookingViewSet`.

| Method | Endpoint | Description | Authentication |
| :--- | :--- | :--- | :--- |
| `GET` | `/api/bookings/` | List all bookings. | Required |
| `POST` | `/api/bookings/` | Create a new booking. | Required |
| `GET` | `/api/bookings/{pk}/` | Retrieve details for a specific booking. | Required |
| `PUT/PATCH`| `/api/bookings/{pk}/` | Update an existing booking record. | Required |
| `DELETE` | `/api/bookings/{pk}/` | Cancel/Delete a booking record. | Required |

---

## 🔒 Permissions & Security

* **`ListingViewSet`:** Uses `IsAuthenticatedOrReadOnly`. Anonymous users can view (`GET`), but must be logged in to create, update, or delete.
* **`BookingViewSet`:** Uses `IsAuthenticatedOrReadOnly`. All operations typically require an authenticated user to ensure booking integrity.

## 📖 API Documentation (Swagger/OpenAPI)

The API is automatically documented using `drf-spectacular`.

| Type | Endpoint | Description |
| :--- | :--- | :--- |
| **Schema** | `/api/schema/` | Raw OpenAPI schema (JSON/YAML). |
| **Swagger UI** | `/api/schema/swagger-ui/` | Interactive documentation for exploring endpoints. |

**To view the documentation, navigate to:** `http://127.0.0.1:8000/api/schema/swagger-ui/`

---

## 🧪 Testing with Postman/cURL

Ensure you have created data in the database and are logged in (e.g., using DRF's built-in login at `/api-auth/login/` or providing an Authorization Token).

### Example: Creating a Listing

```bash
curl -X POST [http://127.0.0.1:8000/api/listings/](http://127.0.0.1:8000/api/listings/) \
-H "Content-Type: application/json" \
-H "Authorization: Token <your_auth_token>" \
-d '{
    "title": "Modern Studio Flat",
    "price": 120.00,
    "description": "A quiet, central place.",
    "max_guests": 2
}'
