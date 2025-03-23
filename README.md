# Serial to TSDB

This project is a Django-based application that reads data from serial devices and stores it in a Time Series Database (TSDB) using ClickHouse and PostgreSQL.

## Features

- User management with Django's built-in authentication system.
- Message handling and storage in ClickHouse.
- RESTful API for interacting with user profiles and messages.
- Dockerized setup for easy deployment.

## Prerequisites

- Docker
- Docker Compose

## Setup

1. Clone the repository:

    ```sh
    git clone https://github.com/moh-skec/serial-to-TSDB.git
    cd serial-to-TSDB
    ```

2. Create a `.env` file in the root directory and set the following environment variables:

    ```env
    DJANGO_SECRET_KEY=your_secret_key
    POSTGRES_DB=postgres
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=your_postgres_password
    CLICKHOUSE_DB=analytics_db
    CLICKHOUSE_USER=default
    CLICKHOUSE_PASSWORD=your_clickhouse_password
    ```

3. Build and start the Docker containers:

    ```sh
    docker-compose up --build
    ```

4. Apply the migrations:

    ```sh
    docker-compose exec web python manage.py migrate
    ```

## Usage

- The application will be available at `http://localhost:8000`.
- The Django admin interface can be accessed at `http://localhost:8000/admin`.

## API Endpoints

### User Profiles

- `GET /user/` - List all user profiles.
- `POST /user/` - Create a new user profile.
- `PUT /user/<int:user_id>/` - Update an existing user profile.
- `DELETE /user/<int:user_id>/` - Delete a user profile.

### Messages

- `GET /msg/` - List all messages.
- `POST /msg/` - Create a new message.
- `PUT /msg/<int:msg_id>/` - Update an existing message.
- `DELETE /msg/<int:msg_id>/` - Delete a message.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
