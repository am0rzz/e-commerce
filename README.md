# E-commerce Product API

This is a RESTful API for a simple e-commerce platform, built with Django and Django REST Framework.

## Features

-   **User Management**: User registration and token-based authentication (login).
-   **Product Management**: Full CRUD (Create, Read, Update, Delete) operations for products.
-   **Search & Filtering**: Endpoints to search products by name/category and apply filters.
-   **Permissions**: Secure endpoints that require authentication for creating or modifying data.
-   **Admin Panel**: Full data management through the built-in Django Admin interface.

## Tech Stack

-   **Backend**: Python, Django, Django REST Framework
-   **Database**: MySQL (or SQLite3 for development)

### Prerequisites

-   Python 3.8+
-   Pip

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/am0rzz/e-commerce.git
    cd ecommerce-api
    ```

2.  **Create and activate a virtual environment:**
    ```sh
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Apply the database migrations:**
    ```sh
    python manage.py migrate
    ```

5.  **Run the development server:**
    ```sh
    python manage.py runserver
    ```
    The API will be available at `http://127.0.0.1:8000/`.

## API Endpoints

Here is a list of the available endpoints.

| Endpoint | Method | Description | Requires Auth |
| ------------------------- | :----: | ------------------------- | :-----------: |
| `/api/users/register/` | `POST` | Register a new user. | No |
| `/api/users/login/` | `POST` | Login to get an auth token. | No |
| `/api/products/` | `GET` | List all products. | No |
| `/api/products/` | `POST` | Create a new product. | Yes |
| `/api/products/<id>/` | `GET` | View a single product. | No |
| `/api/products/<id>/` | `PUT` | Update a product. | Yes |
| `/api/products/<id>/` | `DELETE` | Delete a product. | Yes |

NOTE: I made this readme using AI, so excuse any errors. 
