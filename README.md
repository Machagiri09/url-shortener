# URL Shortener

A simple and efficient URL shortener web application built with Django that converts long URLs into short, shareable links and redirects users to the original URL when accessed. Deployed on Render.

## Features

- Shorten long URLs into compact, unique short links
- Redirect short URLs to their original destination
- Custom alias support for personalized short links
- Click tracking and analytics (total clicks, last accessed)
- Link expiration support
- User authentication for managing personal links (optional)
- REST API for integration with other applications (Django REST Framework)

## Tech Stack

- **Backend:** Django (Python)
- **Database:** PostgreSQL (recommended for Render) / SQLite (for local development)
- **Frontend:** Django Templates / HTML / CSS / JavaScript
- **Hosting:** Render
- **WSGI Server:** Gunicorn

## How It Works

1. The user submits a long URL through the web interface or API.
2. Django generates a unique short code (random string or hash).
3. The mapping between the short code and the original URL is stored in the database.
4. When someone visits the short URL, a Django view looks up the original URL and issues a redirect to it.

## Installation (Local Development)

```bash
# Clone the repository
git clone https://github.com/your-username/url-shortener.git

# Navigate to the project directory
cd url-shortener

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env

# Apply migrations
python manage.py migrate

# Create a superuser (optional, for admin access)
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```

## Environment Variables

| Variable          | Description                              |
|--------------------|---------------------------------------------|
| `SECRET_KEY`       | Django secret key                          |
| `DEBUG`            | Set to `False` in production               |
| `ALLOWED_HOSTS`    | Comma-separated list of allowed hosts       |
| `DATABASE_URL`     | PostgreSQL connection string (Render provides this) |
| `BASE_URL`         | Base URL used for generating short links    |

## Deployment on Render

1. Push the project to a GitHub repository.
2. Create a new **Web Service** on Render and connect your repository.
3. Set the build command:
   ```bash
   pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
   ```
4. Set the start command:
   ```bash
   gunicorn your_project_name.wsgi:application
   ```
5. Add the required environment variables (listed above) in the Render dashboard.
6. Create a PostgreSQL database instance on Render and link the `DATABASE_URL` to your web service.
7. Deploy — Render will build and host the application automatically.

## API Endpoints

| Method | Endpoint                | Description                          |
|--------|--------------------------|---------------------------------------|
| POST   | `/api/shorten/`           | Create a new short URL               |
| GET    | `/<short_code>/`          | Redirect to the original URL         |
| GET    | `/api/stats/<short_code>/` | Get analytics for a short URL       |
| DELETE | `/api/<short_code>/`      | Delete a short URL                   |

### Example Request

```json
POST /api/shorten/
{
  "original_url": "https://www.example.com/some/very/long/url",
  "custom_alias": "my-link"
}
```

### Example Response

```json
{
  "short_url": "https://your-app.onrender.com/my-link",
  "original_url": "https://www.example.com/some/very/long/url",
  "created_at": "2026-06-14T10:00:00Z"
}
```

## Project Structure

```
url-shortener/
├── shortener/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── serializers.py
├── templates/
├── static/
├── your_project_name/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── requirements.txt
├── manage.py
├── .env.example
└── README.md
```

## Future Improvements

- QR code generation for short links
- Bulk URL shortening
- Custom domain support
- Rate limiting and abuse prevention

## License

This project is licensed under the MIT License.
