Product Inventory API

A simple Product Inventory Management System built with **Django**, **Django REST Framework**, and **Docker**.  
It provides REST API endpoints to create, list, update, and delete products.  
Frontend is included with HTML, CSS, and JavaScript for simple product management.

---

Features

- Create, read, update, and delete products via REST API
- Validation: price and stock cannot be negative
- Frontend UI for managing products
- Environment variables for configuration
- Dockerized for easy deployment

---

Technology Stack

- Python 3.11
- Django 5.2
- Django REST Framework
- Docker & Docker Compose
- HTML, CSS, JS

---

Environment Variables

Create a `.env` file at the project root:

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost



**## Setup with Docker**

1. Build and run the containers
docker-compose up --build


--build ensures Docker rebuilds the image

This will start the Django app on http://127.0.0.1:8000


2. Database Migrations

Inside the running container:

docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate

3. Create Superuser (optional)
docker-compose exec web python manage.py createsuperuser



4. Access the App

API: http://127.0.0.1:8000/api/products/
Frontend: http://127.0.0.1:8000/api/




REST API Endpoints


Endpoint	            Method	    Description
/api/products/           GET	    List all products
/api/products/	         POST	    Create a new product
/api/products/<id>/	     PUT	    Update a product
/api/products/<id>/	    DELETE	    Delete a product