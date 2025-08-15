# Django URL Shortener API

This is a RESTful API for a URL shortening service, built with the Django REST Framework. The service allows users to shorten long URLs into unique, compact keys that redirect to the original destination.

## 🚀 Features

* **URL Shortening**: Accepts a long URL and generates a unique, short key.
* **Redirection**: A catch-all route that redirects users from the short URL to the original long URL.
* **Database Integration**: Stores and manages URLs in a SQLite database.
* **Robust Key Generation**: Utilizes a base-62 conversion algorithm with a random key fallback to ensure unique, collision-free short URLs.
* **Error Handling**: Gracefully handles non-existent short keys by returning a `404 Not Found` response.

## 💻 Technologies Used

* **Backend**: Python, Django, Django REST Framework
* **Database**: SQLite
* **Development Environment**: Arch Linux

## ⚙️ How to Run Locally

### Prerequisites
* Django
* pip


### Setup
1.  Clone the repository:
    ```bash
    git clone https://github.com/Appyouz/api_url_shortener.git
    cd api_url_shortener
    ```
2.  Create a virtual environment and activate it:
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```
3.  Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
4.  Configure your  database(if applicable) settings in `settings.py`.
5.  Run database migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
6.  Start the development server:
    ```bash
    python manage.py runserver
    ```

## 📝 API Endpoints

* **Shorten a URL**
    * **Endpoint**: `POST /api/shorten/`
    * **Request Body**: `{"long_url": "https://example.com"}`
    * **Response**: `201 Created` with the new short URL.

* **Redirect to a Long URL**
    * **Endpoint**: `GET /<short_key>/`
    * **Example**: `GET /1/`
    * **Response**: `302 Found` redirect to the original URL or `404 Not Found` if the key doesn't exist.
