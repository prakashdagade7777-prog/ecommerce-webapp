# 🛒 E-Commerce Web Application

A full-featured e-commerce platform built with Python, Django, and PostgreSQL — featuring user authentication, product catalog, and order management.

---

## 🚀 Features

- User registration, login, and authentication (JWT)
- Product catalog with category filtering and search
- Shopping cart and order management
- RESTful API for all operations
- Admin panel for product and order management
- Responsive frontend with HTML/CSS/JavaScript
- Deployed on AWS EC2

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.11 |
| Framework | Django 4.2 + Django REST Framework |
| Database | PostgreSQL |
| Auth | Django Auth + JWT |
| Frontend | HTML5, CSS3, JavaScript |
| Version Control | Git |
| Deployment | AWS EC2 |

---

## 📁 Project Structure

```
ecommerce-webapp/
├── ecommerce/              # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── products/               # Product catalog app
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── orders/                 # Order management app
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── users/                  # User auth app
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── templates/              # HTML templates
├── static/                 # CSS, JS, images
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Run

### Prerequisites
- Python 3.11+
- PostgreSQL
- pip

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/prakashdagade7777-prog/ecommerce-webapp.git
cd ecommerce-webapp

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up PostgreSQL database
createdb ecommerce_db

# 5. Run migrations
python manage.py makemigrations
python manage.py migrate

# 6. Create superuser
python manage.py createsuperuser

# 7. Run server
python manage.py runserver
```

---

## 📬 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/register/` | Register new user |
| POST | `/api/auth/login/` | Login and get token |
| GET | `/api/products/` | List all products |
| GET | `/api/products/{id}/` | Get product details |
| GET | `/api/products/?category=electronics` | Filter by category |
| POST | `/api/orders/` | Create new order |
| GET | `/api/orders/{id}/` | Get order details |

---

## 👤 Author

**Prakash Dagade**
- GitHub: [@prakashdagade7777-prog](https://github.com/prakashdagade7777-prog)
- Email: prakashdagade7777@gmail.com
