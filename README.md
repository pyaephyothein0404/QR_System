# QR Trip Project

## Overview
The QR Trip Project is a Django web application that generates QR codes to redirect users to a responsive trip details page. The application includes user authentication, allowing super users to access specific folders while restricting access to others.

## Features
- QR code generation that links to a trip details page.
- Responsive design for the trip details page.
- User authentication with super user access control.
- Clean and modern UI/UX design.

## Project Structure
```
qr_trip_project
├── manage.py
├── qr_trip_project
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── trip
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
│   ├── templates
│   │   └── trip
│   │       └── trip.html
│   └── static
│       └── trip
│           └── style.css
├── requirements.txt
└── README.md
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd qr_trip_project
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
4. Run database migrations:
   ```
   python manage.py migrate
   ```
5. Create a super user:
   ```
   python manage.py createsuperuser
   ```
6. Start the development server:
   ```
   python manage.py runserver
   ```

## Usage
- Access the application at `http://127.0.0.1:8000/`.
- Generate a QR code that redirects to the trip details page.
- Log in as a super user to access restricted folders.

## License
This project is licensed under the MIT License.