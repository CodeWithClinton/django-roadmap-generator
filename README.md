# Roadmap Generator - Django + OpenAI

This is a Django-based application I built as my final year project while in school, that generates roadmaps using OpenAI's powerful language model.

## Prerequisites

Before running this application, ensure you have the following installed:

- Python 3.6+
- Django
- OpenAI Python library

## Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/CodeWithClinton/django-roadmap-generator.git
```

2. Create and activate your virtual environment
   ```bash
   pip install virtualenvwrapper-win
   mkvirtualenv venv
   ```
   
3. Navigate into the project directory:
```bash
cd personalized_learning
```

4. Install dependencies:
```bash
   pip install -r requirements.txt
```

## Configuration
Obtain an API key from OpenAI by signing up at https://openai.com. <br>
Once you have your API key, create a .env file in the root directory of the project. <br>
Add your OpenAI API key to the .env file:

```bash
OPENAI_API_KEY=your_openai_api_key
```

## Running the Application

1. Apply Migrations
```bash
python manage.py migrate
```
2. Run Development Server
```bash
python manage.py runserver
```
Visit http://127.0.0.1:8000/ in your web browser to access the application.
