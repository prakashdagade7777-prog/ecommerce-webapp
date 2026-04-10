# E-Commerce Web Application

A full-featured e-commerce platform built with Python, Django — featuring user authentication, product catalog, and order management.

---

## Features

- User registration, login, and authentication (JWT)
- Product catalog with category filtering and search
- Shopping cart and order management
- RESTful API for all operations
- Admin panel for product and order management

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.11+ |
| Framework | Django 4.2 + Django REST Framework |
| Database | SQLite (default) |
| Auth | JWT (djangorestframework-simplejwt) |

---

## Project Structure

```
ecommerce-webapp/
├── ecommerce/              # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── products/               # Product catalog app
├── orders/                 # Order management app
├── users/                  # User auth app
├── requirements.txt
└── manage.py
```

---

## Setup & Run

### Step 1 — Go into the project folder
```bash
cd ecommerce-webapp
```

### Step 2 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 3 — Run migrations
```bash
python manage.py migrate
```

### Step 4 — Create admin user (optional)
```bash
python manage.py createsuperuser
```

### Step 5 — Start the server
```bash
python manage.py runserver
```

Open: http://localhost:8000

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API Root |
| POST | `/api/auth/register/` | Register new user |
| POST | `/api/auth/login/` | Login and get JWT token |
| POST | `/api/auth/token/refresh/` | Refresh token |
| GET | `/api/auth/profile/` | User profile (auth required) |
| GET | `/api/products/` | List all products |
| GET | `/api/products/{id}/` | Get product details |
| GET | `/api/products/categories/` | List categories |
| GET/POST | `/api/orders/` | Orders (auth required) |
| GET | `/admin/` | Admin panel |

---

## Login Example

```bash
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "yourpassword"}'
```

Use the returned `access` token in headers:
```
Authorization: Bearer <access_token>
```

---

## Author

**Prakash Dagade**
- GitHub: [@prakashdagade7777-prog](https://github.com/prakashdagade7777-prog)
- Email: prakashdagade7777@gmail.com
