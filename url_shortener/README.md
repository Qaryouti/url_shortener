URL Shortener Service
A simple URL shortener service built with Flask, SQLite, and Python. This service allows users to submit a long URL and receive a shortened version. When the shortened URL is accessed, it redirects to the original long URL.

-Features
URL Shortening: Submit a long URL and get a shortened version.

URL Redirection: Access the shortened URL to be redirected to the original URL.

Persistence: URL mappings are stored in an SQLite database.

Validation: Ensures submitted URLs are valid HTTP/HTTPS URLs.

Rate Limiting: Prevents abuse by limiting requests to 10 per minute per IP.

Frontend: Basic HTML + JavaScript interface for submitting and displaying shortened URLs.

-Setup and Installation
Prerequisites:
Python 3.9.6 (recommended) or any Python 3+ 

pyenv for Python version management (optional but recommended)

venv for virtual environment isolation (optional but recommended)

++Steps to Set Up and Run the Service++
-Clone the Repository

###
git clone https://github.com/Qaryouti/url_shortener
cd url-shortener
###
-Set Up Python Environment

Install pyenv (if not already installed):


Install Python 3.9.6 using pyenv:

###
pyenv install 3.11.8
pyenv local 3.11.8
###
-Activate Virtual Environment

###
source venv/bin/activate  # On Windows: venv\Scripts\activate
###
-Install Dependencies

###
pip install -r requirements.txt
###
-Run the Application

###
python run.py
###
-Access the Service

Open your browser and go to http://127.0.0.1:5000/.

Use the frontend to submit URLs and view shortened links.





-Design Decisions and Assumptions
Database: SQLite is used for simplicity and ease of setup. For production, consider using PostgreSQL or MySQL.

Short Code Generation: Short codes are generated using a hash-based approach with base62 encoding to ensure uniqueness and compactness.

Rate Limiting: Implemented using Flask-Limiter to prevent abuse (10 requests per minute per IP).

Frontend: A basic HTML + JavaScript interface is provided for ease of use.

Validation: URLs are validated to ensure they are valid HTTP/HTTPS URLs.

Duplicate URLs: If the same long URL is submitted multiple times, the same short code is returned.

-Project Structure

###
url-shortener/
├── app/                  # Flask application code
│   ├── __init__.py       # Application factory
│   ├── config.py         # Configuration settings
│   ├── models.py         # Database models
│   ├── routes.py         # API routes
│   └── utils.py          # Helper functions
├── templates/            # HTML templates
│   └── index.html        # Frontend interface
│   └── urls.html         # Frontend interface to show the stored URLs
├── tests/                # Unit tests
│   ├── conftest.py       # Test configuration
│   └── test_routes.py    # Test cases
├── venv/                 # Virtual environment
├── requirements.txt      # Project dependencies
├── run.py                # Application entry point
└── README.md             # Project documentation
###
-Running Tests
To run the unit tests:

###
pytest tests/
###

-Author
This project was built by **Noor Aldeen Qaryouti**.