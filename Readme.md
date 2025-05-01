# FastAPI RBAC Application

This is a FastAPI-based Role-Based Access Control (RBAC) application. The app uses PostgreSQL as the database and includes a PgAdmin service for database management.

## Prerequisites

Ensure you have the following installed on your system:

1. [Docker](https://docs.docker.com/get-docker/)
2. [Docker Compose](https://docs.docker.com/compose/install/)

## Setting Up and Running the Application

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/dileepbc01/Fastapi-RBAC.git
   cd fastapi-rbac
   ```

2. **Set Up Environment Variables**:
   Copy the `.env.example` file to `.env` and update the values as needed:
   ```bash
   cp .env.example .env
   ```

3. **Build and Start the Application**:
   Use Docker Compose to build and start the application:
   ```bash
   docker-compose up --build
   ```

4. **Access the Application**:
   - FastAPI application: [http://localhost:8080](http://localhost:8080)
   - PgAdmin: [http://localhost:5050](http://localhost:5050)


Demo Video: [Watch here](https://drive.google.com/file/d/10OuPOeIZf5oA_RjvloPH5kVpl5LLdC5o/view?usp=sharing)

## Running Services and Ports

The following services are configured and exposed via Docker Compose:

- **Postgres**: Accessible at `localhost:5432`
- **PgAdmin**: Accessible at [http://localhost:5050](http://localhost:5050)
- **FastAPI RBAC Application**: Accessible at [http://localhost:8080](http://localhost:8080)

## API Endpoints

### Authentication
- **POST** `/auth/register`: Register a new user.
- **POST** `/auth/login`: Login and obtain an access token.
- **GET** `/auth/me`: Get the current authenticated user's details.

### Projects
- **GET** `/projects`: Retrieve all projects (requires `view_project` permission).
- **POST** `/projects`: Create a new project (requires `create_project` permission).

## Project Structure

```
.
├── app/
│   ├── api/                # API routes and dependencies
│   ├── schemas/            # Database schemas
│   ├── models/             # Pydantic models
│   ├── utils/              # Utility functions
│   ├── config.py           # Application configuration
│   └── main.py             # Application entry point
├── migrations/             # Database migration files
├── docker-compose.yml      # Docker Compose configuration
├── Dockerfile              # Dockerfile for building the application
├── requirements.txt        # Python dependencies
└── Readme.md               # Project documentation
```