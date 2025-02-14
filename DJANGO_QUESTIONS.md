Here are the answers to the Django interview questions:

---

## **Basic Django Questions**

### **1. What is Django?**  
Django is a high-level Python web framework that enables rapid development of secure and maintainable websites. It follows the **Model-View-Template (MVT)** architecture and provides built-in features like authentication, ORM, and an admin panel.

### **2. How does Django follow the MVT (Model-View-Template) architecture?**  
- **Model:** Defines the database structure (tables and relationships).  
- **View:** Handles business logic and interacts with the model.  
- **Template:** Renders the frontend (HTML).  
Django automatically maps these components, making development faster.

### **3. What are the advantages of using Django?**  
- **Fast development** with built-in features.  
- **Security** (built-in protection against CSRF, XSS, SQL Injection).  
- **Scalability** for handling high traffic.  
- **Batteries included** (ORM, authentication, admin panel, etc.).  

### **4. How do you install Django and create a new project?**  
```bash
pip install django
django-admin startproject myproject
cd myproject
python manage.py runserver
```

### **5. What is the purpose of the `manage.py` file?**  
It’s a command-line utility for managing Django projects, allowing tasks like running the server, applying migrations, and creating apps.

### **6. What are Django apps, and how do they relate to projects?**  
A **Django project** consists of multiple **apps**, which are modular components that handle different features (e.g., a blog app, a user management app). Apps are reusable and can be used across multiple projects.

### **7. What are Django models? How do you define a model in Django?**  
Django models define the database schema. Example:
```python
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```

### **8. How do you run database migrations in Django?**  
```bash
python manage.py makemigrations
python manage.py migrate
```
This generates SQL commands and applies them to the database.

### **9. What are Django views? What is the difference between function-based views (FBVs) and class-based views (CBVs)?**  
Views handle requests and return responses.  
- **FBVs:** Defined as simple Python functions.
- **CBVs:** Use Django’s `View` class and allow reusable behavior.

Example:
```python
from django.http import HttpResponse
from django.views import View

# Function-Based View
def home(request):
    return HttpResponse("Hello, Django!")

# Class-Based View
class HomeView(View):
    def get(self, request):
        return HttpResponse("Hello, Django!")
```

### **10. How does Django handle URLs? Explain the role of `urls.py`.**  
Django uses `urls.py` to map URLs to views.
```python
from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
]
```

### **11. What are Django templates? How do you pass data from views to templates?**  
Templates are HTML files with dynamic placeholders.  
Example:
```html
<h1>Hello, {{ name }}!</h1>
```
Passing data from a view:
```python
def home(request):
    return render(request, "home.html", {"name": "Django"})
```

### **12. What is the purpose of `settings.py` in Django?**  
It contains global settings like database configurations, middleware, installed apps, and static files.

---

## **Intermediate Django Questions**

### **13. How does Django’s ORM work?**  
Django ORM allows querying the database using Python objects instead of raw SQL. Example:
```python
Article.objects.filter(title="Django Guide")
```

### **14. What is the difference between `ForeignKey`, `OneToOneField`, and `ManyToManyField`?**  
- `ForeignKey`: One-to-Many relation  
- `OneToOneField`: One-to-One relation  
- `ManyToManyField`: Many-to-Many relation  

Example:
```python
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

### **15. How do you filter and query data using Django’s ORM?**  
```python
Article.objects.filter(title__icontains="django")
```

### **16. What is middleware in Django?**  
Middleware processes requests before they reach views. Example: authentication, security checks.

### **17. How does Django handle static files and media files?**  
Static files: CSS, JS stored in `/static/`.  
Media files: User uploads, stored in `/media/`.

### **18. What is Django’s authentication system?**  
It includes login, logout, and password management. Example:
```python
from django.contrib.auth.models import User
user = User.objects.create_user(username="john", password="secret")
```

### **19. What are Django signals?**  
Signals allow decoupled components to communicate. Example:
```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
```

### **20. What is the difference between `get()` and `filter()`?**  
- `get()`: Returns a single object, raises `DoesNotExist` if none found.  
- `filter()`: Returns a queryset (multiple results).

---

## **Advanced Django Questions**

### **26. How does Django’s request/response cycle work?**  
1. Request reaches `urls.py`.  
2. Middleware processes it.  
3. View logic executes.  
4. Response is sent to the user.

### **27. Explain the difference between synchronous and asynchronous views in Django.**  
- Traditional Django views are **synchronous**.  
- Django 3.1+ supports **asynchronous views** using `async def`.  

### **28. How do you handle file uploads in Django?**  
```python
class Document(models.Model):
    file = models.FileField(upload_to="uploads/")
```

### **30. What is Django REST framework (DRF)?**  
DRF is a toolkit for building APIs in Django.

### **31. How do you create API views using Django REST framework?**  

```python
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloView(APIView):
    def get(self, request):
        return Response({"message": "Hello, API!"})
```

### **32. What is Django caching, and how does it work?**  

Django supports caching in memory, database, or filesystem.

### **33. How can you optimize database queries in Django?**  

Use `select_related()` and `prefetch_related()` to reduce queries.

### **34. What is Celery, and how can it be integrated with Django?**  

Celery is used for task queues and background jobs.

### **35. How do you handle transactions in Django?**  

Use `atomic`:
```python
from django.db import transaction

with transaction.atomic():
    # Multiple DB operations
```

### **36. How do you write unit tests for Django applications?**  
```python
from django.test import TestCase

class MyTests(TestCase):
    def test_example(self):
        self.assertEqual(1 + 1, 2)
```

### **40. How would you deploy a Django application in production?**  
- Use **Gunicorn** or **uWSGI** as the WSGI server.  
- Use **NGINX** as a reverse proxy.  
- Use **PostgreSQL** or **MySQL** instead of SQLite.  
- Enable **HTTPS** and **load balancing** for scalability.  
