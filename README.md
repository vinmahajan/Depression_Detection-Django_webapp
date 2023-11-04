# Depression Detection Web-App using Django
Depression Detection Using Machine Learning with Twitter Data, Web app version of my Depression Detection Using Machine Learning Project


Follow these steps to set up the project on your local machine.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- pip (Python package manager)
- Virtualenv (optional but recommended)
- Git

## Getting Started

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/vinmahajan/Depression_Detection-Django_webapp.git
   ```

2. Change into the project directory:

   ```bash
   cd Depression_Detection-Django_webapp
   ```

3. Create a virtual environment (recommended):

   ```bash
   # Using virtualenv
   python -m venv venv
   # Activate the virtual environment
   source venv/bin/activate
   # Using pipenv
   pipenv install
   ```

4. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Access the project in your web browser at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


## Contributing

If you'd like to contribute to this project, please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
