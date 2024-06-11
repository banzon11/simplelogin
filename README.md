# Django Simple Login Project

This is a simple Django project that implements basic user authentication.

## Features

- User registration
- User login
- User logout
- Dashboard accessible only to authenticated users

## Setup and Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/banzon11/simplelogin.git
    ```

2. Navigate to the project directory:
    ```bash
    cd simplelogin
    ```

3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply the database migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

The application will be accessible at `http://localhost:8000`.

## Usage

- Visit `http://localhost:8000/signup` to register a new user.
- Visit `http://localhost:8000/login` to log in.
- Visit `http://localhost:8000/dashboard` to view the dashboard (login required).
- Visit `http://localhost:8000/logout` to log out.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

MIT
