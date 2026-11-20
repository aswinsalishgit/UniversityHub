
# UniversityHub

A centralized university operations portal designed to simplify and streamline academic administration through a unified web application.

## Overview

UniversityHub is a web-based project focused on bringing university-related operations into a single platform. Built with Django, it provides a foundation for developing and managing academic workflows.

## Tech Stack

- **Backend:** Python, Django
- **Database:** SQLite
- **Architecture:** Django Applications

## Getting Started

### Prerequisites

- Python 3.x
- pip

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/aswinsalishgit/UniversityHub.git
   cd UniversityHub
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   ```

   Windows:

   ```bash
   venv\Scripts\activate
   ```

   macOS / Linux:

   ```bash
   source venv/bin/activate
   ```

3. Install Django:

   ```bash
   pip install django
   ```

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Open your browser:

   http://127.0.0.1:8000/

## Project Structure

```text
UniversityHub/
├── UniversityHub/
├── academic/
├── manage.py
├── db.sqlite3
└── UniversityHub.code-workspace
```

## License

See the repository for licensing information.
