# BlogApi_DjangoRestFramework
# Django REST API Application

This is a backend REST API application built with Django REST Framework. The application provides APIs for categories, posts, and comments.

## Features

- JWT Authentication
- CRUD operations for categories, posts, and comments

## Installation

1. Clone the repository
    ```
    git clone <repository_url>
    ```

2. Navigate to the project directory
    ```
    cd <project_directory>
    ```

3. Install the requirements
    ```
    pip install -r requirements.txt
    ```

## Running the Application

1. Apply migrations
    ```
    python manage.py migrate
    ```

2. Run the server
    ```
    python manage.py runserver
    ```

## API Endpoints

- `/api/categories/` : GET, POST, PUT, DELETE operations for categories.
- `/api/posts/` : GET, POST, PUT, DELETE operations for posts.
- `/api/comments/` : GET, POST, PUT, DELETE operations for comments.

## Authentication

This application uses JWT for authentication. To authenticate, send a POST request to `/api/token/` with your username and password.

## Testing

To run tests:
```
python manage.py test
```

## Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.

