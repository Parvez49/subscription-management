# Subscription Management System

A simple Django-based project with support for:
- User Registration & Login using JWT
- Subscription Plans (Free, Monthly, Yearly)
- Celery + Celery Beat for background tasks
- Simple HTML frontend for viewing subscriptions

---

## 🛠️ Local Setup

1. **Clone the repository**

```bash
git clone https://github.com/Parvez49/subscription-management.git
cd subscription-management
```

2. Create and activate a virtual environment
```
python -m venv venv
source venv/bin/activate
```
3. Install dependencies
```
pip install -r requirements/local.txt
```
4. Run migrations
```
python manage.py migrate
```
5. Load default subscription plans(Optional)
```
python manage.py load_plans
```
6. Run development server
```
python manage.py runserver
```

## ⚙️ Celery & Celery Beat
1. Start Redis
```
# On Ubuntu
sudo service redis-server start
```
2. Run Celery worker
```
celery -A config worker --loglevel=info
```
3. Run Celery Beat
```
celery -A config beat --loglevel=info
```

If using local settings and set in config/settings/local.py:
```
CELERY_TASK_ALWAYS_EAGER = True
```

Note: Do not need to run Celery/Beat for development/testing purposes — tasks run synchronously.


## 🧪 API Endpoints
### 🔐 Auth
Register
```
POST /api/v1/register/

{
  "username": "username",
  "email": "email@example.com",
  "password": "pass123"
}
```
Login (Get JWT tokens)
```
POST /api/v1/login/

{
  "username": "username",
  "password": "pass123"
}
```

### 📦 Subscriptions (Protected)

Must pass Authorization: Bearer <access_token> in headers.
Create Subscription
```
POST /api/v1/subscribe/

{
  "plan": <plan_id>
}
```
List My Subscriptions
```
GET /api/v1/subscriptions/
```

## Project Structure

```
<repository_root>/
├── config/
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── local.py
│   │   └── production.py
│   ├── __init__.py
│   ├── asgi.py
│   ├── celery.py
│   ├── urls.py
│   └── wsgi.py
├── <django_project_root>/
│   ├── <app_name>/
│   │   ├── api/
│   │   │   ├── <version>/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── filters.py
│   │   │   │   ├── serializers.py
│   │   │   │   ├── urls.py
│   │   │   │   └── views.py
│   │   │   ├── __init__.py
│   │   │   └── urls.py
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tasks.py
│   │   ├── tests.py
│   │   ├── signals.py
│   │   ├── utils.py
│   │   └── views.py
│   ├── __init__.py/
│   └── ...
├── requirements/
│   ├── base.txt
│   ├── local.txt
│   └── production.txt
├── venv/
├── .env
├── manage.py
```
